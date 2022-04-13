import os
import pvaccess as pva
import numpy as np
import queue
import time
import threading
import signal
import json

from pathlib import Path
from amcontrols import util
from amcontrols import log
from epics import PV


class AMControls():
    """ Class for controlling Additive Manufacturing apparatus via EPICS

        Parameters
        ----------
        args : dict
            Dictionary of pv variables.
    """

    def __init__(self, pv_files, macros):

        # init pvs
        self.config_pvs = {}
        self.control_pvs = {}
        self.pv_prefixes = {}
        
        if not isinstance(pv_files, list):
            pv_files = [pv_files]
        for pv_file in pv_files:
            self.read_pv_file(pv_file, macros)
        self.show_pvs()

        # Define PVs we will need from the sample x-y-z motors, which is on another IOC

        example_pv_name = self.control_pvs['Example'].pvname
        self.control_pvs['ExamplePosition']      = PV(example_pv_name + '.VAL')


        # Define PVs from the camera IOC that we will need
        prefix = self.pv_prefixes['Camera']
        camera_prefix = prefix + 'cam1:'

        self.control_pvs['CamAcquireTime']          = PV(camera_prefix + 'AcquireTime')
        self.control_pvs['CamArraySizeXRBV']        = PV(camera_prefix + 'ArraySizeX_RBV')
        self.control_pvs['CamArraySizeYRBV']        = PV(camera_prefix + 'ArraySizeY_RBV')

        self.epics_pvs = {**self.config_pvs, **self.control_pvs}
        
        # print(self.epics_pvs)
        for epics_pv in ('DefocusSelect', ):
            self.epics_pvs[epics_pv].add_callback(self.pv_callback)

        # Start the watchdog timer thread
        thread = threading.Thread(target=self.reset_watchdog, args=(), daemon=True)
        thread.start()

        log.setup_custom_logger("./amcontrols.log")

        self.epics_pvs['AMStatus'].put('All good!')

    def reset_watchdog(self):
        """Sets the watchdog timer to 5 every 3 seconds"""
        while True:
            self.epics_pvs['Watchdog'].put(5)
            time.sleep(3)

        log.setup_custom_logger("./amcontrols.log")

    def read_pv_file(self, pv_file_name, macros):
        """Reads a file containing a list of EPICS PVs to be used by AMControls.


        Parameters
        ----------
        pv_file_name : str
          Name of the file to read
        macros: dict
          Dictionary of macro substitution to perform when reading the file
        """

        pv_file = open(pv_file_name)
        lines = pv_file.read()
        pv_file.close()
        lines = lines.splitlines()
        for line in lines:
            is_config_pv = True
            if line.find('#controlPV') != -1:
                line = line.replace('#controlPV', '')
                is_config_pv = False
            line = line.lstrip()
            # Skip lines starting with #
            if line.startswith('#'):
                continue
            # Skip blank lines
            if line == '':
                continue
            pvname = line
            # Do macro substitution on the pvName
            for key in macros:
                pvname = pvname.replace(key, macros[key])
            # Replace macros in dictionary key with nothing
            dictentry = line
            for key in macros:
                dictentry = dictentry.replace(key, '')

            epics_pv = PV(pvname)

            if is_config_pv:
                self.config_pvs[dictentry] = epics_pv
            else:
                self.control_pvs[dictentry] = epics_pv
            # if dictentry.find('PVAPName') != -1:
            #     pvname = epics_pv.value
            #     key = dictentry.replace('PVAPName', '')
            #     self.control_pvs[key] = PV(pvname)
            if dictentry.find('PVName') != -1:
                pvname = epics_pv.value
                key = dictentry.replace('PVName', '')
                self.control_pvs[key] = PV(pvname)
            if dictentry.find('PVPrefix') != -1:
                pvprefix = epics_pv.value
                key = dictentry.replace('PVPrefix', '')
                self.pv_prefixes[key] = pvprefix

    def show_pvs(self):
        """Prints the current values of all EPICS PVs in use.

        The values are printed in three sections:

        - config_pvs : The PVs that are part of the scan configuration and
          are saved by save_configuration()

        - control_pvs : The PVs that are used for EPICS control and status,
          but are not saved by save_configuration()

        - pv_prefixes : The prefixes for PVs that are used for the areaDetector camera,
          file plugin, etc.
        """

        print('configPVS:')
        for config_pv in self.config_pvs:
            print(config_pv, ':', self.config_pvs[config_pv].get(as_string=True))

        print('')
        print('controlPVS:')
        for control_pv in self.control_pvs:
            print(control_pv, ':', self.control_pvs[control_pv].get(as_string=True))

        print('')
        print('pv_prefixes:')
        for pv_prefix in self.pv_prefixes:
            print(pv_prefix, ':', self.pv_prefixes[pv_prefix])

    def pv_callback(self, pvname=None, value=None, char_value=None, **kw):
        """Callback function that is called by pyEpics when certain EPICS PVs are changed
        """

        log.debug('pv_callback pvName=%s, value=%s, char_value=%s', pvname, value, char_value)
        if (pvname.find('DefocusSelect') != -1) and ((value == 0) or (value == 1)):
            thread = threading.Thread(target=self.yes_no_select, args=())
            thread.start()

    def yes_no_select(self):
        """Plot the cross in imageJ.
        """

        if (self.epics_pvs['DefocusSelect'].get() == 0):
            rayleigh_length_value = self.epics_pvs['RayleighLength'].get()
            self.epics_pvs['RayleighLength'].put(rayleigh_length_value/2.0)
            log.info('divide by 2: %f' % rayleigh_length_value)
            self.epics_pvs['AMStatus'].put('divide by 2')
        else:
            rayleigh_length_value = self.epics_pvs['RayleighLength'].get()
            self.epics_pvs['RayleighLength'].put(rayleigh_length_value*2.0)
            log.info('Multiply by 2: %f' % rayleigh_length_value)
            self.epics_pvs['AMStatus'].put('multiply by 2')

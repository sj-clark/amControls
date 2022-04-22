=====
Usage
=====

Start EPICS IOC
---------------

::

    fast@merlot $ cd ~/epics/synApps/support/amcontrols/iocBoot/iocAMControls
    fast@merlot $ ./start_IOC

at the end of the start up process you will get the IOC console::

   Starting iocInit
   ############################################################################
   ## EPICS R7.0.6.2-DEV
   ## Rev. R7.0.6.1-75-g91941af992f6c32ef4f4
   ############################################################################
   reboot_restore: entry for file 'auto_settings.sav'
   reboot_restore: Found filename 'auto_settings.sav' in restoreFileList.
   *** restoring from './autosave/auto_settings.sav' at initHookState 6 (before record/device init) ***
   reboot_restore: done with file 'auto_settings.sav'

   reboot_restore: entry for file 'auto_settings.sav'
   reboot_restore: Found filename 'auto_settings.sav' in restoreFileList.
   *** restoring from './autosave/auto_settings.sav' at initHookState 7 (after record/device init) ***
   reboot_restore: done with file 'auto_settings.sav'

   cas WARNING: Configured TCP port was unavailable.
   cas WARNING: Using dynamically assigned TCP port 44367,
   cas WARNING: but now two or more servers share the same UDP port.
   cas WARNING: Depending on your IP kernel this server may not be
   cas WARNING: reachable with UDP unicast (a host's IP in EPICS_CA_ADDR_LIST)
   iocRun: All initialization complete
   create_monitor_set("auto_settings.req", 30, "P=32id:,R=AMControls:")
   save_restore:readReqFile: unable to open file amControls.req. Exiting.
   epics> auto_settings.sav: 8 of 8 PV's connected
   epics>

If you do any modification to the **amControls_settings.req** or **amControls.template** files in::

   ~/epics/synApps/support/amcontrols/amcontrolsApp/Db

you neeed to rebuld the epics IOC::

   epics> exit
   fast@merlot $ cd ../..
   fast@merlot $ make -sj
   fast@merlot $ cd iocBoot/iocAMControls

and restart the IOC::

   fast@merlot $ ./start_IOC

You can accomplish the same with a single line command::

   fast@merlot $ cd ../.. ; make -sj ; cd iocBoot/iocAMControls ; ./start_IOC


Start MEDM screen
-----------------

::

    fast@merlot $ cd ~/epics/synApps/support/amcontrols/iocBoot/iocAMControls
    fast@merlot $ ./start_medm

.. image:: img/amControls.png 
   :width: 720px
   :align: center
   :alt: am_user

or::

  fast@merlot $ ./start_medm_user

.. image:: img/amControls_main.png 
   :width: 720px
   :align: center
   :alt: am_user


Start python server
-------------------

::

    $ bash
    (base) $ conda activate amcontrols
    (amcontrols) fast@merlot $ cd ~/epics/synApps/support/amcontrols/iocBoot/iocAMControls
    (amcontrols) fast@merlot $ python -i start_amcontrols.py
    configPVS:
    CameraPVPrefix : 2bmbSP2:
    ExamplePVName : 32id:m1
    DefocusSelect : Positive
    RayleighLength : 50.00
    BeamWaist : 0
    BeamWaistYPosition : 0
    DesiredBeamDiameter : 0
    SampleHeight : 0
 
    controlPVS:
    Example : None
    Go : Done
    AMStatus : 
    Watchdog : -38
 
    pv_prefixes:
    Camera : 2bmbSP2:
    >>>

If you do any modification to the python source code files in::

   ~/epics/synApps/support/amcontrols/amcontrols/

you neeed to rebuld the python server code::

   >>> exit()
   (amcontrols) fast@merlot $ cd ../..
   (amcontrols) fast@merlot $ python setup.py install
   (amcontrols) fast@merlot $ cd iocBoot/iocAMControls/
   (amcontrols) fast@merlot $ python -i start_amcontrols.py

You can accomplish the same with a single line command::

   (amcontrols) fast@merlot $ cd ../../; python setup.py install; cd iocBoot/iocAMControls/; python -i start_amcontrols.py




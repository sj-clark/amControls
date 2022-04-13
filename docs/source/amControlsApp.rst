===============================
amcontrolsApp EPICS application
===============================

.. 
   toctree::
   :hidden:

   amcntrols.template
   amcontrols_settings.req
   amcontrols.substitutions


amControls includes a complete example EPICS application, including:

- A database file and corresponding autosave request file that contain the PVs required by the amcontrols.py base class.
- OPI screens for medm
- An example IOC application that can be used to run the above databases.
  The databases are loaded in the IOC with the example substitutions file, 
  :doc:`amControls.substitutions`.


Base class files
================
The following tables list all of the records in the amControls.template file.
These records are used by the amcontrols base class and so are required.

amControls.template
-------------------

This is the database file that contains only the PVs required by the amcontrol.py base class
:doc:`amControls.template`.

Example PV Prefixes
^^^^^^^^^^^^^^^^^^^

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)CameraPVPrefix
    - stringout
    - Contains the prefix for the detector, e.g. 2bmbSP2:

Example PV name
---------------

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)ExamplePVName
    - stringout
    - Contains a PV name, e.g. 32id:m1

AM served PVs
^^^^^^^^^^^^^

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)RayleighLength
    - ao
    - Contains the Rayleigh Length value
  * - $(P)$(R)BeamWaist
    - ao
    - Contains the BeamWaist value
  * - $(P)$(R)BeamWaistYPosition
    - ao
    - Contains the BeamWaistYPosition value
  * - $(P)$(R)DesiredBeamDiameter
    - ao
    - Contains the DesiredBeamDiameter value
  * - $(P)$(R)SampleHeight
    - ao
    - Contains the SampleHeight value

Defocus select
^^^^^^^^^^^^^^

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)DefocusSelect
    - mbbo
    - Defocus direction selector, Positive or Negative


AM status via Channel Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)Go
    - busy
    - Setting this record to 1 starts a control action.
  * - $(P)$(R)AMStatus
    - waveform
    - This record will be updated with the scan status while scanning.
  * - $(P)$(R)ServerRunning
    - bi
    - This record will be ``Running`` if the Python server is running and ``Stopped`` if not.
      It is controlled by a watchdog timer, and will change from ``Running`` to ``Stopped``
      within 5 seconds if the Python server exits.

medm files
----------

amControls.adl
^^^^^^^^^^^^^^

The following is the MEDM screen :download:`amControls.adl <../../amcontrolsApp/op/adl/amControls.adl>` during a scan. 
The status information is updating.

.. image:: img/amControls.png
    :width: 75%
    :align: center

amControlsEPICS_PVs.adl
^^^^^^^^^^^^^^^^^^^^^^^

The following is the MEDM screen :download:`amControlsEPICS_PVs.adl <../../amcontrolsApp/op/adl/amControlsEPICS_PVs.adl>`. 

If these PVs are changed amControls must be restarted.

.. image:: img/amControlsEPICS_PVs.png
    :width: 75%
    :align: center


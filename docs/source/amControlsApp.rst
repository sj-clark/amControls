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

Camera PV Prefixes
------------------

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)CameraPVPrefix
    - stringout
    - Contains the prefix for the detector, e.g. 2bmbPG1:

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

Optique Peter camera selector
-----------------------------

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)CameraSelect
    - mbbo
    - Fast shutter selector for Pos0 and Pos1 position
  * - $(P)$(R)CameraPos0
    - a0
    - Motor position for the first camera
  * - $(P)$(R)CameraPos1
    - a0
    - Motor position for the second camera
  * - $(P)$(R)CameraName0
    - a0
    - Camere label for Pos0, e.g. Adimec
  * - $(P)$(R)CameraName1
    - a0
    - Camera label for Pos1, e.g. Flir
  * - $(P)$(R)CameraLock
    - bo
    - Camera lock
  * - $(P)$(R)CameraMotorPVName
    - stringout
    - Contains the camera motor PV name, e.g. 2bmb:m5

Optique Peter lens selector
---------------------------

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)LensSelect
    - mbbo
    - Lens selector for Pos0 and Pos1 position
  * - $(P)$(R)LensPos0
    - a0
    - Motor position for the first lens
  * - $(P)$(R)LensPos1
    - a0
    - Motor position for the second lens
  * - $(P)$(R)LensPos2
    - a0
    - Motor position for the third lens
  * - $(P)$(R)LensName0
    - a0
    - Lens label for Pos0, e.g. 10x
  * - $(P)$(R)LensName1
    - a0
    - Lens label for Pos1, e.g. 5x
  * - $(P)$(R)LensName2
    - a0
    - Lens label for Pos2, e.g. 1.1x
  * - $(P)$(R)LensLock
    - bo
    - Lens lock
  * - $(P)$(R)LensMotorPVName
    - stringout
    - Contains the Lens motor PV name, e.g. 2bmb:m1

Optics information
^^^^^^^^^^^^^^^^^^

.. cssclass:: table-bordered table-striped table-hover
.. list-table::
  :header-rows: 1
  :widths: 5 5 90

  * - Record name
    - Record type
    - Description
  * - $(P)$(R)ScintillatorType
    - stringout
    - Contains the type of scintillator being used.
  * - $(P)$(R)ScintillatorThickness
    - ao
    - Contains the thickness of the scintillator in microns.
  * - $(P)$(R)ImagePixelSize
    - ao
    - Contains the pixel size on the sample in microns (i.e. includes objective magnification)
  * - $(P)$(R)DetectorPixelSize
    - ao
    - Contains the pixel size of the detector.
  * - $(P)$(R)CameraObjective
    - stringout
    - Description of the camera objective
  * - $(P)$(R)CameraTubeLength
    - stringout
    - Description of the camera objective

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

If these PVs are changed tomoscan must be restarted.

.. image:: img/amControlsEPICS_PVs.png
    :width: 75%
    :align: center


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
  * - $(P)$(R)amControlsPv1
    - stringout
    - Contains a string PV.
  * - $(P)$(R)amControlsPv1
    - ao
    - Contains a float PV.
  * - $(P)$(R)amControlsPv1
    - ao
    - Contains a float PV.
  * - $(P)$(R)amControlsPv1
    - ao
    - Contains a float PV.
  * - $(P)$(R)amControlsPv1
    - stringout
    - Contains a string PV.
  * - $(P)$(R)amControlsPv1
    - stringout
    - Contains a string PV.

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


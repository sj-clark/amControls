TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = amControlsApp

# amControlsApp.dbd will be created and installed
DBD += amControlsApp.dbd

# test.dbd will include these files:
amControlsApp_DBD += base.dbd
amControlsApp_DBD += busySupport.dbd
amControlsApp_DBD += asSupport.dbd

# amControlsApp_registerRecordDeviceDriver.cpp derives from test.dbd
amControlsApp_SRCS += amControlsApp_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
amControlsApp_SRCS_DEFAULT += amControlsMain.cpp
amControlsApp_SRCS_vxWorks += -nil-

amControlsApp_LIBS += autosave
amControlsApp_LIBS += busy
#amControlsApp_LIBS += asyn

# Finally link IOC to the EPICS Base libraries
amControlsApp_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

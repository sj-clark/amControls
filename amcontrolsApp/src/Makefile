TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = amcontrolsApp

# amcontrolsApp.dbd will be created and installed
DBD += amcontrolsApp.dbd

# test.dbd will include these files:
amcontrolsApp_DBD += base.dbd
amcontrolsApp_DBD += busySupport.dbd
amcontrolsApp_DBD += asSupport.dbd

# amcontrolsApp_registerRecordDeviceDriver.cpp derives from test.dbd
amcontrolsApp_SRCS += amcontrolsApp_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
amcontrolsApp_SRCS_DEFAULT += amcontrolsMain.cpp
amcontrolsApp_SRCS_vxWorks += -nil-

amcontrolsApp_LIBS += autosave
amcontrolsApp_LIBS += busy
#amcontrolsApp_LIBS += asyn

# Finally link IOC to the EPICS Base libraries
amcontrolsApp_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

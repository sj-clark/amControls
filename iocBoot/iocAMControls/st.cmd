< envPaths

epicsEnvSet("P", "32id:")
epicsEnvSet("R", "AMControls:")

## Register all support components

# Use these lines to run the locally built amControlsApp
dbLoadDatabase "../../dbd/amControlsApp.dbd"
amControlsApp_registerRecordDeviceDriver pdbbase



dbLoadTemplate("amControls.substitutions")

< save_restore.cmd
save_restoreSet_status_prefix($(P))
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=$(P)")

iocInit

create_monitor_set("auto_settings.req", 30, "P=$(P),R=$(R)")

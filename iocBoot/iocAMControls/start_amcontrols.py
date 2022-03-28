# This script creates an object of type AMControls for doing tomography streaming reconstruction
# To run this script type the following:
#     python -i start_amcontrols.py
# The -i is needed to keep Python running, otherwise it will create the object and exit
from amcontrols.amcontrols import AMControls
ts = AMControls(["../../db/amControls_settings.req","../../db/amControls_settings.req"], {"$(P)":"32id:", "$(R)":"AMControls:"})

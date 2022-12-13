timeout -k 4h 4h sh solversACC-standby.sh > ACC-standby.log
timeout -k 4h 4h sh solversACC-following.sh > ACC-following.log
timeout -k 4h 4h sh solversACC-speedcontrol.sh > ACC-speedcontrol.log
timeout -k 4h 4h sh solversACC-error.sh > ACC-error.log
timeout -k 4h 4h sh solversACC-hold.sh > ACC-hold.log
timeout -k 4h 4h sh solversACC-override.sh > ACC-override.log

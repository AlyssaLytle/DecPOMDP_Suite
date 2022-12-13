timeout -k 4h 4h sh solversACC-incexp-standby.sh > ACC-incexp-standby.log
timeout -k 4h 4h sh solversACC-incexp-following.sh > ACC-incexp-following.log
timeout -k 4h 4h sh solversACC-incexp-speedcontrol.sh > ACC-incexp-speedcontrol.log
timeout -k 4h 4h sh solversACC-incexp-error.sh > ACC-incexp-error.log
timeout -k 4h 4h sh solversACC-incexp-hold.sh > ACC-incexp-hold.log
timeout -k 4h 4h sh solversACC-incexp-override.sh > ACC-incexp-override.log

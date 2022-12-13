timeout -k 4h 4h sh solversACC-cluster-standby.sh > ACC-cluster-standby.log
timeout -k 4h 4h sh solversACC-cluster-following.sh > ACC-cluster-following.log
timeout -k 4h 4h sh solversACC-cluster-speedcontrol.sh > ACC-cluster-speedcontrol.log
timeout -k 4h 4h sh solversACC-cluster-error.sh > ACC-cluster-error.log
timeout -k 4h 4h sh solversACC-cluster-hold.sh > ACC-cluster-hold.log
timeout -k 4h 4h sh solversACC-cluster-override.sh > ACC-cluster-override.log

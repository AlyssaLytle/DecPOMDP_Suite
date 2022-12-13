sh ClearResults.sh
echo "Running:solversACC-noopt-standby.sh"
timeout -k 4h 4h sh solversACC-noopt-standby.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-standby.log
echo "Running:solversACC-noopt-following.sh"
timeout -k 4h 4h sh solversACC-noopt-following.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-following.log
echo "Running:solversACC-noopt-speedcontrol.sh"
timeout -k 4h 4h sh solversACC-noopt-speedcontrol.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-speedcontrol.log
echo "Running:solversACC-noopt-error.sh"
timeout -k 4h 4h sh solversACC-noopt-error.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-error.log
echo "Running:solversACC-noopt-hold.sh"
timeout -k 4h 4h sh solversACC-noopt-hold.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-hold.log
echo "Running:solversACC-noopt-override.sh"
timeout -k 4h 4h sh solversACC-noopt-override.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-noopt-override.log

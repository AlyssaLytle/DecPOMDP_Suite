echo "Running:solversACC-standby.sh"
timeout -k 4h 4h sh solversACC-standby.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-standby.log
echo "Running:solversACC-following.sh"
timeout -k 4h 4h sh solversACC-following.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-following.log
echo "Running:solversACC-speedcontrol.sh"
timeout -k 4h 4h sh solversACC-speedcontrol.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-speedcontrol.log
echo "Running:solversACC-error.sh"
timeout -k 4h 4h sh solversACC-error.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-error.log
echo "Running:solversACC-hold.sh"
timeout -k 4h 4h sh solversACC-hold.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-hold.log
echo "Running:solversACC-override.sh"
timeout -k 4h 4h sh solversACC-override.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-override.log

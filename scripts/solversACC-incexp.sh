sh ClearResults.sh
echo "Running:solversACC-incexp-standby.sh"
timeout -k 4h 4h sh solversACC-incexp-standby.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-standby.log
echo "Running:solversACC-incexp-following.sh"
timeout -k 4h 4h sh solversACC-incexp-following.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-following.log
echo "Running:solversACC-incexp-speedcontrol.sh"
timeout -k 4h 4h sh solversACC-incexp-speedcontrol.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-speedcontrol.log
echo "Running:solversACC-incexp-error.sh"
timeout -k 4h 4h sh solversACC-incexp-error.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-error.log
echo "Running:solversACC-incexp-hold.sh"
timeout -k 4h 4h sh solversACC-incexp-hold.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-hold.log
echo "Running:solversACC-incexp-override.sh"
timeout -k 4h 4h sh solversACC-incexp-override.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-incexp-override.log

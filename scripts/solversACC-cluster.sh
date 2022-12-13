sh ClearResults.sh
echo "Running:solversACC-cluster-standby.sh"
timeout -k 4h 4h sh solversACC-cluster-standby.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-standby.log
echo "Running:solversACC-cluster-following.sh"
timeout -k 4h 4h sh solversACC-cluster-following.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-following.log
echo "Running:solversACC-cluster-speedcontrol.sh"
timeout -k 4h 4h sh solversACC-cluster-speedcontrol.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-speedcontrol.log
echo "Running:solversACC-cluster-error.sh"
timeout -k 4h 4h sh solversACC-cluster-error.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-error.log
echo "Running:solversACC-cluster-hold.sh"
timeout -k 4h 4h sh solversACC-cluster-hold.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-hold.log
echo "Running:solversACC-cluster-override.sh"
timeout -k 4h 4h sh solversACC-cluster-override.sh > /afs/cs.unc.edu/home/abyrnes1/public/alyssadpomdp/DecPOMDP_Suite/logs/ACC-cluster-override.log

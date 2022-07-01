cd ../MADP/src/utils
date +%T
echo "Finding value for QMDP"
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QMDP > QMDP.log
date +%T
echo "Finding value for QPOMDP"
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDP > QPOMDP.log
date +%T
#echo "Finding value for QBG"
#timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBG > QBG.log
#date +%T
# echo "Finding value for QMDPc"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QMDPc > QMDPc.log
# date +%T
# echo "Finding value for QPOMDPav"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDPav > QPOMDPav.log
# date +%T
# echo "Finding value for QBGav"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGav > QBGav.log
# date +%T
# echo "Finding value for QHybrid"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QHybrid > QHybrid.log
# date +%T
# echo "Finding value for QPOMDPhybrid"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDPhybrid > QPOMDPhybrid.log
# date +%T
# echo "Finding value for QBGhybrid"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGhybrid > QBGhybrid.log
# date +%T
# echo "Finding value for QBGTreeIncPrune"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGTreeIncPrune > QBGTreeIncPrune.log
# date +%T
# echo "Finding value for QBGTreeIncPruneBnB"
# timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGTreeIncPruneBnB > QBGTreeIncPruneBnB.log
# date +%T

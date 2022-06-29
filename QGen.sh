cd ../MADP/src/utils
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QMDP > QMDP.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDP > QPOMDP.log
#timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBG > QBG.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QMDPc > QMDPc.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDPav > QPOMDPav.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGav > QBGav.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QHybrid > QHybrid.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QPOMDPhybrid > QPOMDPhybrid.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGhybrid > QBGhybrid.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGTreeIncPrune > QBGTreeIncPrune.log
timeout -k 1h 1h ./calculateQheuristic ~/public/alyssadpomdp/DecPOMDP_Suite/MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 -Q QBGTreeIncPruneBnB > QBGTreeIncPruneBnB.log

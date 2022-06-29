date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 
date +%T

date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 > min_pol.txt
date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse  MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 > min_pol2.txt
date +%T
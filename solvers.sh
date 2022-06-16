date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC-min/ACC-standby-s1.dpomdp -h1 > min_pol.txt
date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2 > full_pol.txt
date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC/ACC-ss-standby-scen-1-obs.dpomdp -h2 > full_pol_obs.txt
date +%T
../MADP/src/solvers/GMAA --verbose --verbose --sparse  MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2 > min_pol2.txt
date +%T
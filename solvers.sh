timeout -k 30m 30m ../MADP/src/solvers/GMAA --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC-min/ACC-standby-s1.dpomdp -h2
timeout -k 30m 30m ../MADP/src/solvers/GMAA --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC/ACC-ss-standby-scen-1.dpomdp -h2
timeout -k 30m 30m ../MADP/src/solvers/GMAA --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob MADPtools/ACC/ACC-ss-standby-scen-1-obs.dpomdp -h2

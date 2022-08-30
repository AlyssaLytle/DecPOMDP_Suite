cd ..
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s0.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s1.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s2.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s3.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s4.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s5.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s6.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-speedcontrol-s7.dpomdp -h2

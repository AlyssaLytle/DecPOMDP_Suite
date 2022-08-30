cd ..
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s0.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s1.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s2.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s3.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s4.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s5.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s6.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-following-s7.dpomdp -h2

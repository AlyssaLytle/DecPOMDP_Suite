cd ..
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s0.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s1.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s2.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s3.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s4.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s5.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s6.dpomdp -h2
timeout -k 1h 1h ../MADP/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-override-s7.dpomdp -h2

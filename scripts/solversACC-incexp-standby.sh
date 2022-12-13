cd ..
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s0.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s1.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s2.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s3.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s4.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s5.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s6.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-standby-s7.dpomdp -h2

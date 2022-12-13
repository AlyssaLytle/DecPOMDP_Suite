cd ..
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s0.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s1.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s2.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s3.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s4.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s5.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s6.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC-incexp/ACC-incexp-error-s7.dpomdp -h2

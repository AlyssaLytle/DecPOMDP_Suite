cd ..
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s0.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s1.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s2.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s3.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s4.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s5.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s6.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-hold-s7.dpomdp -h2

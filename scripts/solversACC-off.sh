cd ..
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s0.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s1.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s2.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s3.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s4.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s5.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s6.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC/ACC-off-s7.dpomdp -h2

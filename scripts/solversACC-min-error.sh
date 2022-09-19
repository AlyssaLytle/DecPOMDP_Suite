cd ..
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s0.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s1.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s2.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s3.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s4.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s5.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s6.dpomdp -h2
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar  --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob  -Q QMDP --useQcache MADPtools/ACC-min/ACC-min-error-s7.dpomdp -h2

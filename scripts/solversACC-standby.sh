cd ..
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s0.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s1.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s2.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s3.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s4.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s5.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s6.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-standby-s7.dpomdp -h2

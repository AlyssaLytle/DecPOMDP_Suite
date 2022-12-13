cd ..
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s0.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s1.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s2.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s3.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s4.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s5.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s6.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --useBGclustering -Q QMDP MADPtools/ACC-cluster/ACC-cluster-override-s7.dpomdp -h2

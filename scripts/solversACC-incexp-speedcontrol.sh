cd ..
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s0.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s1.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s2.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s3.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s4.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s5.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s6.dpomdp -h2
now="$(date +'%M:%S:%3N')"
echo "Time: $now"
timeout -k 1h 1h ../MADP2/src/solvers/GMAA --sparse --GMAA=MAAstar --BGIP_Solver=BnB --BnB-ordering=Prob -Q QMDP MADPtools/ACC/ACC-speedcontrol-s7.dpomdp -h2

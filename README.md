# File Descriptions
- ArrayTree.py: Class that implements tree structures as arrays
- MADP_types_gen.py: Generates scripts to solve dpomdps and generate Q values
- ClearResults.sh: !!DANGER!! clears result files

## TexOutputs - Generates Tex Outputs from Results

## scripts - Shell scripts to run many solvers at once

## MADPtools - Code to generate, run, and analyze examples on MADP toolbox
- ACCtest.sh: Shell script that tests many different solvers on MADP toolbox
- dpomdp.csv: Stores information of Decpomdp to be read later, updated when MADP_types_gen.py is run
- listresults.sh: prints results and stores them in "lsOutput.log"
- MADPtools (dir): tools to write .dpomdp files for the MADP solver
  - DPOMDP_Writer (dir): Contains "writer" class
    - DPOMDPWriterMedium.py: Main class for decpomdp creation. Includes value methods as well.
    - ExtractCSV.py: reads a state transition table from a csv file, used in DPOMDPWriterMedium
    - Reader.py: can read MADP toolbox's output files and make trees
    - TransitionLatexClean.csv: state transition table for ACC
  - AnalyzeResults.py: Reads output file names from lsOutput.log and saves the policy tree values
  - SanityChecks.py: Some methods to make sure .dpomdp files are being generated correctly
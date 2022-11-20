# AI6128_MapMatching_assignment 

## Assignment codes all here  
Relevant file names:  
Final_Report.doc - Final report content  
postprocessed_output.csv - Output of map match algorithm. Contains rows of mapped route for each trajectory.  
porto_big - contains saved network of the porto_big network graph used for task 6. It also contain the output result of various SP Dist settings and the FMM algorithm log file.  
porto_whole1 - contains saved network of the porto_whole1 network graph used for task 3 and task 4.  
Task2_src.ipynb  
task3_fmm.py - The python script called to run the FMM algorithm map matching that was recommended by assignment instruction.  
Task3_src.ipynb - Source code to preprocess and postprocess the output of FMM algorithm task3_fmm.py script.  
Task4_src.ipynb  
Task5_src.ipynb - Source code to generate the 5 road segments that are traversed the most, and average traveling computing using the map matched trajectory data file postprocessed_output.csv.  
data - folder containing the output data of Task5_src.ipynb. output data contains the approximate average traverse time(in seconds) of each segment ID (defined as network's edge ID) and the frequency of how road segment usage as per the 1000 trajectory.
Task6_src.ipynb - Source code to generate visualization figures used in the report of Task 6.  

## Setup instructions:
Required packages: tqdm, osmnx, numpy, csv, matplotlib, geopandas  
Task 2 Visualization code - Task2_src.ipynb  
Task 3 Pre-process/post-process code Task3_src.ipynb (can be executed by ensuring the folder 'porto_whole1' is in the same directory as source code file)   
Task 4 Visualization code - Task4_src.ipynb  
Task 5(1), 5(2) and 5(3) code - Task5_src.ipynb (can be executed by ensuring the folder 'porto_whole1' is in the same directory as source code file)   
Task 6 Figures Visualization code - Task6_src.ipynb (can be executed by ensuring the folder 'porto_big' is in the same directory as source code file)  

Task 3 FMM code
Requires a system running on Ubuntu Focal and FMM Toolkit installed following the author's instruction here: https://fmm-wiki.github.io/docs/installation/ubuntu.html  
task3_fmm.py was run with command "python task3_fmm.py"
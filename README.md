# AI6128_MapMatching_assignment 

## Assignment codes all here  
Relevant file names:  
  
1. AI6128 Assignment Final_Report.doc - Final report content  
  
2. postprocessed_output.csv - CSV File storing the mapped routes of all 1000 trajectories in the train-1000 dataset from Task 3. Pre-built, output of map match algorithm. Each row contains 1 mapped route for each trajectory.  
  
3. porto_big - contains saved network of the porto_big network graph used for task 6. It also contain the output result of various SP Dist settings and the FMM algorithm log file.  
  
4. porto_whole1 - contains saved network of the porto_whole1 network graph used for task 3 and task 4.  
  
5. Task2_src.ipynb - Create 10 Visualization of Raw GPS points and plot them on 10 figures using matplotlib and osmnx  
  
6. task3_fmm.py - The python script called to run the FMM algorithm map matching that was recommended by assignment instruction. This code read input trajectory data from the pre-processed file trips_time.txt, which was provided by Task1_src.ipynb.    
  
7. Task3_src.ipynb - Source code to preprocess and postprocess the output of FMM algorithm task3_fmm.py script.  
  
8. Task4_src.ipynb - Create 10 Visualization of Raw GPS points and plot them on 10 figures using matplotlib and osmnx  
  
9. Task5_12_src.ipynb - Source code to generate the 5 road segments that are traversed the most, and average traveling computing using the map matched trajectory data file postprocessed_output.csv.  
  
10. Task5_3_src.ipynb - Visualization of Task 5 output  

11. data - folder containing train_1000.csv and the output data of Task5_12_src.ipynb. output data contains the approximate average traverse time(in seconds) of each segment ID (defined as network's edge ID) and the frequency of how road segment usage as per the 1000 trajectory.  
  
12. Task6_src.ipynb - Source code to generate visualization figures used in the report of Task 6.  
  
## Setup instructions:
Required packages: tqdm, osmnx, numpy, csv, matplotlib, geopandas  
  
1. Task 1 Preprocess code - Task1_src.ipynb - Execute by ensuring the full trajectory kaggle data is saved as 'train.csv' in the 'data' folder. Produces train_1000.csv and time.txt (input data file for FMM)   
  
2. Task 2 Visualization Generation code - Task2_src.ipynb - Execute by ensuring train_1000.csv is located in the data folder. ensure descartes package install in python environment    
  
3. Task 3 FMM Post-process code - Task3_src.ipynb - Execute by ensuring the original submitted folder, 'porto_whole1' is in the same directory as source code file.
Postprocess will convert FMM output from file name porto_whole1/porto_whole1_output.txt into a new file postprocessed_output.csv for Task 4 and Task 5 work.  
  
4. Task 4 Visualization Generation code - Task4_src.ipynb - Execute by ensuring all of porto_whole1 is original as per submission and that postprocessed_output.csv is in same directory of script file  
  
5. Task 5(1), 5(2) code - Task5_12_src.ipynb - Execute by ensuring the original submitted folder, 'porto_whole1' is in the same directory as source code file  
  
6. Task 5(3) code - Task5_3_src_ipynb - Execute by ensuring the folder 'data' and the original submitted folder, 'porto_whole1' is in the same directory as source code file
  
7. Task 6 Figures Visualization code - Task6_src.ipynb - Majority of the visualization code take some time to run. Execute by ensuring the original submitted folder, 'porto_whole1' is in the same directory as source code file  
  
  
Task 3 FMM code  
Requires a system running on Ubuntu Focal and FMM Toolkit installed following the author's instruction here: https://fmm-wiki.github.io/docs/installation/ubuntu.html   
  
8. Task 3 FMM Algorithm computing code using Python API of FMM algorithm - task3_fmm.py - Execute by ensuring the original submitted folder, 'porto_whole1' in the the same directory as source code file. Run with terminal command "python task3_fmm.py". 
Wait for generation of UBODT file and map matching routes file to be produced as postprocessed_output.csv in the porto_whole1 folder.    

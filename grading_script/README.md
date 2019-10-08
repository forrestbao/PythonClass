# Automatically grading of programming assignments 

The scripts are for grading programming assignments automatically 
from Python scripts that students submitted. 
This set of scripts can be used for any software testing purposes. 

# How it works

The grading scripts generate one Python script based on each student-submitted
script. 
The generated Python script imports functions from student-uploaded Python scripts
(which contains function definitions),
then call those functions giving appropriate randomly generated data, 
compare with the expected outcome, 
and finally writes the grading results into a text file.
A Bash script then runs all generated Python scripts. 

# Files 
1. `main_hw3.py` is a template including the grading functions and the generation of random testing data. 
2. `combine.py` produces the Python script to be run for grading based one student-submitted script and the `main_hw3.py`
3. `lib_hw3.py` contains functions definitions that are solutions to the homework -- hence not uploaded here.
4. `grade.bash` A Bash script that does all errands and runs `combine.py` and all generated scripts. 

# License 
GNU GPL 3+

Copyleft 2019 Forrest Sheng Bao  

- Task: realize Naive Algoritm for searching a substring in string.


- How to execute: 
1) Download a project from github: `git clone https://github.com/VKasaraba/Algorithms_lab.git`
2) Open naive_algo_in_csv and write your string on the 1st line, and the pattern on the 2nd line.
	Example:
	Internet Of Things
	i

3) Open runner.py and execute the script.
4) Open naive_algo_out_csv to see a result. The result will be an array, which consists start positions
of pattern substring found in string. For the examle above, whe result must be:
	'Substrings fround at positions: [0, 14]'

Important: the algorihm ignores lowercase and uppercase. To to distinguish the register, comment lines 4 and 5 
in naive_algoritm.py.

Additional: to run tests, go to naive_algorithm_test.py and execute the command 'python -m unittest naive_algorithm_test' 
in the local terminal.


- Description of the algorithm:
Naive algorithm is exact string matching.  It iterates through each symbol of the input string (due too for-loop on line 13 in 
naive_algoritm.py), and compares the input pattern to the part of the input string, lenght of wich is equal to the pattern lenght
(due too while-loop on line 15 in naive_algoritm.py).

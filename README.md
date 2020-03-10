# PythonPrograms
Python Programs for practise

### Sudoku solver - sample output 
```
$ python sudoku_solver.py

[0, 0, 0, 0, 0, 3, 9, 0, 1]
[4, 0, 0, 2, 0, 5, 8, 3, 0]
[0, 6, 0, 8, 0, 0, 2, 0, 0]
[0, 0, 8, 0, 5, 0, 0, 9, 0]
[0, 2, 0, 0, 4, 0, 0, 5, 0]
[0, 3, 0, 0, 8, 0, 6, 0, 0]
[0, 0, 3, 0, 0, 1, 0, 8, 0]
[0, 1, 4, 6, 0, 8, 0, 0, 2]
[8, 0, 6, 5, 0, 0, 0, 0, 0]


Solved !!!

[5, 8, 2, 4, 7, 3, 9, 6, 1]
[4, 9, 1, 2, 6, 5, 8, 3, 7]
[3, 6, 7, 8, 1, 9, 2, 4, 5]
[6, 4, 8, 1, 5, 2, 7, 9, 3]
[7, 2, 9, 3, 4, 6, 1, 5, 8]
[1, 3, 5, 9, 8, 7, 6, 2, 4]
[2, 5, 3, 7, 9, 1, 4, 8, 6]
[9, 1, 4, 6, 3, 8, 5, 7, 2]
[8, 7, 6, 5, 2, 4, 3, 1, 9]
```

### Rangoli of english alphabets - sample output
```
$ python Rangoli.py
Enter size of Rangoli (1 for a, 2 for b....26 for z): 12
----------------------l----------------------
--------------------l-k-l--------------------
------------------l-k-j-k-l------------------
----------------l-k-j-i-j-k-l----------------
--------------l-k-j-i-h-i-j-k-l--------------
------------l-k-j-i-h-g-h-i-j-k-l------------
----------l-k-j-i-h-g-f-g-h-i-j-k-l----------
--------l-k-j-i-h-g-f-e-f-g-h-i-j-k-l--------
------l-k-j-i-h-g-f-e-d-e-f-g-h-i-j-k-l------
----l-k-j-i-h-g-f-e-d-c-d-e-f-g-h-i-j-k-l----
--l-k-j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j-k-l--
l-k-j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j-k-l
--l-k-j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j-k-l--
----l-k-j-i-h-g-f-e-d-c-d-e-f-g-h-i-j-k-l----
------l-k-j-i-h-g-f-e-d-e-f-g-h-i-j-k-l------
--------l-k-j-i-h-g-f-e-f-g-h-i-j-k-l--------
----------l-k-j-i-h-g-f-g-h-i-j-k-l----------
------------l-k-j-i-h-g-h-i-j-k-l------------
--------------l-k-j-i-h-i-j-k-l--------------
----------------l-k-j-i-j-k-l----------------
------------------l-k-j-k-l------------------
--------------------l-k-l--------------------
----------------------l----------------------
```


### Function as a service (FaaS version of above Rangoli - FaasRangoli.py)
```
Hit below URL in browser, modify size parameter (between 1 to 26),
https://us-central1-faas-270704.cloudfunctions.net/Rangoli?size=20 
```

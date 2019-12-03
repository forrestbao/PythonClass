# Lab on advanced topics

## 1. The highest and lowest grade of a class [2pt

Suppose you are given a dictionary whose keys are the names of students and the values are their corresponding numerical grades, compute the highest and the lowest grades of the class. Define a function called `grade_range`, which takes the aforementioned dictionary as the sole input and returns two numbers, which are the lowest (first) and highest (second) grades of the class. 

Below are 4 test cases. For simplicity, the students have numerical names from 0 to 9. 

```
{'0': 10, '1': 36, '2': 7, '3': 4, '4': 40, '5': 13, '6': 5, '7': 51, '8': 56, '9': 71} # return 4, 71
{'0': 1, '1': 10, '2': 53, '3': 4, '4': 45, '5': 47, '6': 80, '7': 32, '8': 87, '9': 60}  
{'0': 45, '1': 66, '2': 34, '3': 53, '4': 63, '5': 92, '6': 82, '7': 72, '8': 10, '9': 35}
{'0': 70, '1': 67, '2': 41, '3': 46, '4': 97, '5': 97, '6': 16, '7': 26, '8': 17, '9': 9} 

```

Do NOT use the Python's built-in function `max` or `min`. Instead, iterate over the values by yourself. 

## 2. Recursion: valid perfect square [3pt]

A square number (4, 9, 16, ...) has a numerical property that it is a sum of all odd numbers under it. [Here](https://www.geeksforgeeks.org/check-number-is-perfect-square-using-additionsubtraction/) is an explanation and sample code in Python 3. 

Now try to solve it recursively. Denote the number to be checked as `n`. Here is the idea: Starting from `i=1`, gradually subtract `i` from `n`. Increase `i` by 2 each time. If at one point, the `n` becomes 0, then return True. If `n` falls below 0, then return False. 

One way to do so is to define the function that takes two arguments as input. Denote the function as `is_square(n,i)`.  Let the inductive case be `is_square(n-i, i+2)`  -- thus subtract `i` from `n` and increase `i` by 2 for the next time. The base case is when `n<0`, where you should return False, or when `n==0`, where you return True. You always call the function with `i=1`. For example, to check whether `4` or `36` is a square number, you call the function as `is_square(4,1)` or `is_square(36,1)`, respectively. 

Of course, feel free to explore your own approach to do it recursively. You do not have to use the method above. 

Below is a table showing how the function recurses itself with differen `n`'s and `i`'s for checking 16. 

|n|i| note | 
|--|--|--| 
|16|1| `is_square(16,1)` is the same as `is_square(15,3)`  |
|15|3| `is_square(15,3)` is the same as `is_square(12,5)` | 
|12|5| `is_square(12,5)` is the same as `is_square(7,7) ` | 
|7|7|  `is_square(7,7)` is the same as `is_square(0,9) ` | 
|0|9|   base case. perfect. no residue. return True | 

Below is another example for checking 15. 

|n|i| note | 
|--|--|--| 
|15|1| `is_square(15,1)` is the same as `is_square(14,3)`  |
|14|3| `is_square(14,3)` is the same as `is_square(11,5)` | 
|11|5| `is_square(11,5)` is the same as `is_square(6,7) ` | 
|6|7|  `is_square(6,7)` is the same as `is_square(-1,9) ` | 
|-1 |9|   base case. n false below 0. Return False   | 

# Lab 4 Part 2: For-loops and lists (continued)

Author: Forrest Sheng Bao, Computer Science, Iowa State University, Ames, IA, USA

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Factorials
Define a function `FactorialCy` that takes a number `x` as the input and returns the factorial of `x`. For example, `FactorialCy(4)` returns 24 (4x3x2x1). Hint: Using one for-loop that iterates from `x` to 2. 

## MacLaurin series. 
Recall that in Lab 1 we manually entered an expression to calculate MacLaurin series for exponential to a finite number of terms. Now let's do it to a very high precision. 
Define a function `MyExp`, that takes a number (integer or floating-point) `x` and an integer `p` as inputs and returns exp(x) calculated with up to `p` non-constant terms. For example, `MyExp(2, 3)` returns `1 + 2 + 2^2/2! + 2^3/3!`. You may call the `FactorialCy` function defined above. 
Compute the expoential of a few numbers you pick in `MyExp` with different `p` values. See whether the result is approximating to the answer you can get from a calculator gradually as `p` increases. 

Wikipedia has a visualization on the approximation getting more accurate with more terms: (https://en.wikipedia.org/wiki/Taylor_series#/media/File:Exp_series.gif)

## Diff 

Difference (short as diff) is an operation commonly performed in scientific computing, and thus is provided in many libraries:  

* NumPy (a common library for numerical computation in Python): (https://docs.scipy.org/doc/numpy/reference/generated/numpy.diff.html)
* MATLAB (an evil and ugly language): (https://www.mathworks.com/help/matlab/ref/diff.html)
* Mathematica: (https://reference.wolfram.com/language/ref/Differences.html)

Now, implement your own `diff` in Python. Given a list `X` of numbers, `diff(X)` returns `X[0]-X[1], X[1]-X[2], ...`

Optional: Implement it without using indexes. Instead, first create a new list `Y = [X[1], X[2], ...]` using slicing operation (e.g., `X[2:5]`), then zip `X` and `Y`, and finally do pairwise subtraction on the zipped list of 2-tuples. 

## Diff and sign 
Define a function `DiffSign` that given a list `X` of numbers, returns a binary (+1 and -1) list `Y`  such that Y[i] is +1 if X[i] > X[i+1] and -1 otherwise. For example, `DiffSign([1,8, 4, 2])` returns `[-1, 1, 1]`. Do so using the method we discussed in class. 

## A full Caeser cipher

In HW3, the string encoder and decoder are provided by the instructor. 
Please re-implement the two functions, `scramble` and `restore` using for-loops. Hint: just apply your single-character encoder and decoder, respectively, onto each character in a string. Then run the demo given in HW3.

## Split a sentence into words
Define a function `chunk` that takes a string as input, and then returns a list consisting of all space-separated elements of the string. 
For example, `chunk("I am happy.  ")} shall return `["I", "am", "happy."]`. Hint: Scan the string, if a character is not space, append it into a temporary string; if it is, end the temporary string and append it to a list, and reset the temporary string to empty. The list should be empty initially too. 

## Crack the Caesar cipher (optional)

The Caesar cipher is actually super easy to crack if you know a word that must be included in the encrypted message, the ciphertext. For example, 
To be continued as a week-long project. 

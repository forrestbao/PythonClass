# Lab 4 Part 3: For-loops and lists (continued)

Author: Forrest Sheng Bao, Computer Science, Iowa State University, Ames, IA, USA

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

## Square root approximated 
Define a function `SqrtInt` that takes a number (integer or float-point number) `x` as the input and returns an integer closest to the square root of `x`. For example, `SqrtInt(17.3)` returns 4 (because 4<sup>2</sup>=16, and 5<sup>2</sup>=25, but 16 is closer to 17.3 than 25).  Assume that `x` is greater than 1. 

To solve this problem, you first need to find two integers, denoted as `a` and `b` such that a<sup>2</sup><=x and b<sup>2</sup>>= x, and b-a = 1. To do so, use a for-loop, to sequentially check all integers from 1 to `int(x)`. 

For example, for `SqrtInt(17.3)`, do this:

*  Let i be 1. Is 1^2 <=17.3 and (1+1)^2 >= 17.3? No, so keep going. 
*  Let i be 2. Is 2^2 <=17.3 and (2+1)^2 >= 17.3? No, so keep going.
*  Let i be 3. Is 3^2 <=17.3 and (3+1)^2 >= 17.3? No, so keep going.
*  Let i be 4. Is 4^2 <=17.3 and (4+1)^2 >= 17.3? Yes! 
	* Now, check whether 4^2 or 5^2 is closer to 17.3. 
		* Since 17.3-16<25-17.3, 4 is the number we need.
		*  Return 4. (All remaining iterations (rounds) skipped.  )

Turn this into a for-loop.

## Buying a house? 
Do Parts A and B of this problem set from MIT. 
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/MIT6_0001F16_ps1.pdf)




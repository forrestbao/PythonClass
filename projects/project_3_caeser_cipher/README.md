
## General idea
Given an encrypted message in which only lower case Latin letters are shifted while other characters inact, there 26 different ways to decrypt this message. 
Among the 26 ways, some of them will result in a message consisting of non-existing words. 
For example, if the plain message is 'happy', then the encrypted message of shift 2 is 'jcrra'. 
Given 'jcrra', unless you know the shift is 2, you will still get a gebbrish, e.g., 'ibqqz' if you guess the shift is 1. 

The idea to crack a Caeser cipher is to decrypt the message in 26 ways, and pick the one way that contain the most legitmate English words. 

## Step 0: ASCII code

Digital computers use numbers to store every kind of information, even movies and video games.
So every character you see on the computer, e.g., a Twitter message, it actually an integer beneath the surface. 
In particular, the computer uses something called the ASCII code to store basic latin characters, Arabic numericals, some punctuations, and control strings.
ASCII code ranges from 1 to 127. 
For example:
* All upper case letters A-Z are of ASCII code 65 ('A') to 90 ('Z'), continously.
* All lower case letters a-z are of ASCII code 97 ('a') to 122 ('z'), continously.
* All Arabic digits 0-9 are of ASCII code 48 ('0') to 57 ('9'), continously.
* The space is a character of ASCII code 32.   

Python provides two functions to convert between a character and its integer "true identity":
* Given a character, to get its ASCII code, you can use the `ord` function. 
* Given an integer in ASCII code, to get the corresponding character (if any), you can use the `cha` function. 

Here are some examples (in iPython format): 
```
In [10]: ord('B')
Out[10]: 66

In [11]: chr(67)
Out[11]: 'C'
```

Now, define a function `ascii2string` that take a list of integers as the input, 
and returns a string consistsing of their corresponding characters in ASCII. 
You may safely assume that all those integers are between 48 and 122.  
(Hint: use `join` function. See advanced topics notes.)

Then, define another function `char2string` that takes a string as the input, 
and returns a list of integers of their correponding number in ASCII. 
You may assume that this string contains only a-z, A-Z, 0-9, and space. 

Test examples for `ascii2char` and `char2ascii`: 
| integer list | string |
|------|-------|
| [69, 69, 71, 73, 100, 101] | `EEGIde`  |


## Step 1: Building the single-character encrypter and decrypter

**We only en/de-crypt lower case Latin letters. Leave other characters, including digits and upper case letters inact.**

Now, since you know that a character is actually stored in the computer as an integer, we can save the 27-way if-statement 
as you did in HW3. 
Instead, you can encrypt a character by simply doing `chr(ord(x)+s)` where `x` is a character and `s` is the position to shift. 
For example, `chr(ord('a')+2)` gives you letter `c` which is the letter `a` shifted 2 positions forward. 

However, the non-trivial part is the wrapping. For example, `chr(ord('z')+2)` does not give you `b` but `|`. 
Here is one way: or a-z, if the shifted ascii number goes beyond 122, subtract it by 26. 
Here is a more detailed example: given letter `z` with a shift of 4, the encrypted character is `chr(ord('z')+4-26)` which is `d`.

So implement one function, `encrypt1` of two arguments:
1. a character, that is to be encrypted, and
2. an integer, representing the amount that the character should be shifted to, considering wrapping. 
If the input character is a lower case Latn letter (ASCII code between and including 97 and 122), encrypt it. Otherwise, leave it inact.

You might wanna use a if-else statement to handle the cases that shifting goes beyond the boundary and not. 

Some test cases (in iPython style) : 
```
In [40]: caeser.encrypt1('z', 3)
Out[40]: 'c'

In [41]: caeser.encrypt1('z', 1)
Out[41]: 'a'

In [42]: caeser.encrypt1('a', 3)
Out[42]: 'd'

In [43]: caeser.encrypt1('a', 1)
Out[43]: 'b'

In [44]: caeser.encrypt1('A', 1)
Out[44]: 'A'

In [45]: caeser.encrypt1('Y', 4)
Out[45]: 'Y'

In [47]: caeser.encrypt1('9', 1)
Out[47]: '9'

```

Finally, in this step, implement the inverse of the `encrypt1` function, named as `decrypt1`. 

Some test cases:
```
In [52]: caeser.decrypt1('1', 3)
Out[52]: '1'

In [54]: caeser.decrypt1('Z', 1)
Out[54]: 'Z'

In [56]: caeser.decrypt1('d', 3)
Out[56]: 'a'

In [57]: caeser.decrypt1('d', 4)
Out[57]: 'z'

```


## Step 2: Expanding the single-character encrypter and decrypter into string encrypter and decrypter. 
 
In the step above, a single character can be encrypted or descrypted. 
Now define two new functions to expand your capability to encrypt and decrypt a string. 
The new functions `encrypt_string` and `decrypt_string`, both have two arguments:
1. a string, to be en/de-crypted
2. an integer, the shift to encrypt or used to encrypt the string. 

Same test cases (note that lower case letters and numericals are wrapped separately) :
```
In [3]: caeser.encrypt_string('ddsaf', 4)
Out[3]: 'hhwej'

In [4]: caeser.decrypt_string('hhwej', 4)
Out[4]: 'ddsaf'

In [5]: caeser.encrypt_string('sdafdsf.sdfdsf.23323', 4)
Out[5]: 'whejhwj.whjhwj.23323'

In [6]: caeser.decrypt_string('whejhwj.whjhwj.67767', 4)
Out[6]: 'sdafdsf.sdfdsf.67767'

In [8]: caeser.encrypt_string('sdafdsf.sdfdsf.23323', 8)
Out[8]: 'alinlan.alnlan.23323'

In [10]: caeser.decrypt_string('alinlan.alnlan.01101', 8)
Out[10]: 'sdafdsf.sdfdsf.01101'
```

## Step 3: Load an English dictionary from file

A key to crack a Caeser cipher is to check the overlap between words in the decrypted message and words in a dictionary. 
For example, the message 'q eqtt amm gwc wv acvlig 11 iu' is most likely resulted from encrypting the message 'i will see you on sunday 11 am' with a shift of 8. Other shift amounts will result in words that are mostly nonexisting in English. 

So, let's load a text file that contains 10,000 most frequent English words and save the 10,000 words as a list of strings. 
Define a function `load_dict` that takes one string as the sole input, which is the path to the file on your computer, and returns a dictionary of strings. 

The text file can be downloaded from.... 
Each line is one English word in lower case. So when you load it, be sure to remove the newline character using the `strip` function (see Advanced Topics). 

## Step 4: Check the overlap of words between a decrypted message and a dictionary

Now, given a decrypted message, we want to check the ratio of  words in it being legitemate  English words. 
First, split the decrypted message into a list of words using the `split` functin for strings (see Advanced Topics). 
Then think how to count the number of same elements given two list. In our case, one of the two lits is  the list of words splitted from the decrypted message, while the other is the list of 10,000 English words. 
Finally, return the ratio of legitmate English words in the decrypted message. 

## Step 5: Put things together 


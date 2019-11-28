Project Caeser cipher cracker 

## General idea
Given an encrypted message in which only lower case Latin letters are shifted while other characters unchanged, there 26 different ways to decrypt this message. 
Among the 26 ways, some of them will result in a message consisting of non-existing words. 
For example, if the plain message is 'happy', then the encrypted message of shift 2 is 'jcrra'. 
Given 'jcrra', unless you know the shift is 2, you will still get a gebbrish, e.g., 'ibqqz' if you guess the shift is 1. 

The idea to crack a Caeser cipher is to decrypt the message in 26 ways, and pick the one way that contain the most legitmate English words. 

Note that we only en/de-crypt lower case letters. All other characeters, including upper case, digits, and punctuations, are left alone. 

## Step 0: ASCII code

Digital computers use numbers to store every kind of information, even movies and video games.
Every character you see in a text data, e.g., a Twitter message, it actually an integer beneath the surface. 
In particular, the computer uses something called the ASCII codes to store basic latin characters, Arabic numericals, some punctuations, and control strings.
ASCII codes range from 1 to 127. 
For example:

* All upper case letters A-Z are of ASCII codes 65 ('A') to 90 ('Z'), continously.
* All lower case letters a-z are of ASCII codes 97 ('a') to 122 ('z'), continously.
* All Arabic digits 0-9 are of ASCII codes 48 ('0') to 57 ('9'), continously.
* The space is a character of ASCII codes 32.   

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

Now, define a function `ascii2string` that takes a list of integers as the input, 
and returns a string consistsing of their corresponding characters in ASCII. 
You may safely assume that all those integers are between 48 and 122.  
(Hint: use `join` function to concatenate a list of characters into a string. See advanced topics notes.)

Then, define another function `string2ascii` that takes a string as the input, 
and returns a list of their ASCII codes. 
You may assume that this string contains only a-z, A-Z, 0-9, and space. 

Test examples for `ascii2string` and `string2ascii`: 

| integer list | string |
|------|-------|
| [69, 69, 71, 73, 100, 101] | `EEGIde`  |
| [50, 60, 70 ,80, 90, 100] | `2<FPZd` | 
| [55, 65, 75, 85, 95, 105, 115]  | `7AKU_is`  |

## Step 1: Building the single-character encrypter and decrypter

**We only en/de-crypt lower case Latin letters. Leave other characters, including digits and upper case letters unchanged.**

Now, since you know that a character is actually stored in the computer as an integer, we can replace the 27-way if-statement 
as you did in HW3 by an expression to increase the ASCII code of the character. 
In detail, you can encrypt a character by simply doing `chr(ord(x)+s)` where `x` is a character and `s` is the position to shift. 
For example, `chr(ord('a')+2)` gives you letter 'c' which is the letter 'a' shifted 2 positions forward. 

However, the non-trivial part is the wrapping. For example, `chr(ord('z')+2)` does not give you 'b' but '|'. 
Here is one workaround: For a-z, if the shifted ASCII code goes beyond 122, subtract it by 26. 
Here is a more detailed example: given letter 'z' with a shift of 4, the encrypted character is `chr(ord('z')+4-26)` which is 'd'.

So implement one function, `encrypt1` of two arguments:

1. a character, that is to be encrypted, and
2. an integer, representing the amount that the character should be shifted to, considering wrapping. 
If the input character is a lower case Latin letter (ASCII code between and including 97 and 122), encrypt it. Otherwise, leave it unchanged.

You might wanna use an if-else branch to handle the cases that shifting goes beyond the boundary and not. 

Some test cases (in iPython style, suppose the function `encrypt` is in a module `caeser`) : 

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
2. an integer, the shift to en/de-crypt the string. 

Some test cases:

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
Define a function `load_english` that takes one string as the sole input, which is the path to the file on your computer, and returns a dictionary of strings. 

The text file can be downloaded from https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt 
Each line is one English word in lower case. So when you load it, be sure to remove the newline character using the `strip` function (see Advanced Topics). 

## Step 4: Check the overlap of words between a decrypted message and a dictionary

Now, given a decrypted message (one of the 26 ways to decrypt), check the ratio of  words in it being legitemate  English words. 
First, split the decrypted message into a list of words, denoted as `L1`, using the `split` function for strings (see Advanced Topics). 
Then scan the words in the list `L1`. For each word check whether it is also a member of the list of legitemate English words, denoted as `L2`, loaded in the previous step.
Finally, return the ratio of legitmate English words in the decrypted message. 

Name this function as `check_legit` and let the 1st and 2nd arguments be `L1` and `L2` respectively. Note once again, the first argument is the decrypted message (which may be full of gebbrish) and the second argument is the list of 10,000 English words.

Some test cases (the 2nd argument is a very short list of English words but not 10,000):

```
In [23]: caeser.check_legit(['happy', 'sad', 'lucky', 'dfd'],['happy', 'lucky'])
Out[23]: 0.5

In [24]: caeser.check_legit(['happy', 'sad', 'lucky', 'dfd'],['happy'])
Out[24]: 0.25

In [25]: caeser.check_legit(['happy', 'sad', 'lucky', 'dfd'],['happy', 'lucky', 'good', 'bad'])
Out[25]: 0.5

In [26]: caeser.check_legit(['happy', 'good', 'lucky', 'dfd'],['happy', 'lucky', 'good', 'bad'])
Out[26]: 0.75
``` 


## Step 5: Put things together 

Now put everything together in the right order and dependency to define an overall function called `crack` that takes one encrypted message as input and return the best decrypted message. 

Here is the pseudocode:

```
best_score = 0 
best_shift = i 
for i from 0 to 25:
    decrypt the message with shift i (using decrypt_string function) 
    let x be  the ratio of words in the decrypted message be legitemate English words (use the check_legit function)
    if x > best_score:
         let best_shift  be i  
         let best_score be x 

return decrypted message with shfit best_shift 
```

Some test cases:


| input | output |
|---|---|
| 'xli pyrgl aew GREAT' | 'the lunch was GREAT' |
| 'xli qiixmrk mw ex 11 eq' | 'the meeting is at 11 am' | 
| 'xli fiiv mw $9'  | 'the beer is $9'  |


## Submission and grading 
Turn in one Python 3 script, named as `yourlastname_yourfirstname_caeser.py`

In the file, include the definitions of all these functions:

* `ascii2string`  1pt
* `string2ascii`  1pt
* `encrypt1`     2pt
* `decrypt1`     2pt
* `encrypt_string`  3pt
* `decrypt_string`  3pt
* `load_english`   2pt
* `check_legit`    2pt
* `crack`          4pt


## Bonus (10 points in final grading):
To crack a simple Caeser cipher is not tedious: just trying 26 ways. Hence a more crack-proof Caeser cipher is to allow different shifts for different letters. For example, letter 'a' shifts 3 positions, letter 'b' shifts 6 positions, letter 'c' shifts 1 position, etc. In this case, to crack, `26^26 = 6,156,119,580,207,157,310,796,674,288,400,203,776` combinations need to be checked. 
Define a function `crack_pro` to crack a message encrypted in this way.  Feel free to 

If you do not fully get how to cracked the simple Caeser cipher, this bonus part will take you a lot of time. It may be easier to earn 10 points in final grading by doing well in the final exam than doing this bonus problem. However, if you fully understand every thing above, it shouldn't take you more than 50% of the time that it took you to solve the non-bonus part. Hint: just expand certain functions from one for-loop to two nested for-loops, the inner of which tries decrypt one letter in 26 possibilities and the outter of which scans over all 26 letters. 

Because `26^26` is a huge number, let's assume that each letter will be shifted by either 1 or 2 positions forward. In this case, your program just need to search for `2^26 = 67,108,864` possibilities. 


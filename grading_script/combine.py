# runs for Python 2 because Python3 has no StringIO 

import glob
import StringIO, tokenize

with open("main_hw3.py", "r")  as f:
    main_body = f.read()

def remove_comments_and_docstrings(source):
    """
    Returns 'source' minus comments and docstrings.

    this function is taken from 
    https://stackoverflow.com/questions/1769332/script-to-remove-python-comments-docstrings

    """
    io_obj = StringIO.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        # The following two conditionals preserve indentation.
        # This is necessary because we're not using tokenize.untokenize()
        # (because it spits out code with copious amounts of oddly-placed
        # whitespace).
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        # Remove comments:
        if token_type == tokenize.COMMENT:
            pass
        # This series of conditionals removes docstrings:
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
        # This is likely a docstring; double-check we're not inside an operator:
                if prev_toktype != tokenize.NEWLINE:
                    # Note regarding NEWLINE vs NL: The tokenize module
                    # differentiates between newlines that start a new statement
                    # and newlines inside of operators such as parens, brackes,
                    # and curly braces.  Newlines inside of operators are
                    # NEWLINE and newlines that start new code are NL.
                    # Catch whole-module docstrings:
                    if start_col > 0:
                        # Unlabelled indentation means we're inside an operator
                        out += token_string
                    # Note regarding the INDENT token: The tokenize module does
                    # not label indentation inside of an operator (parens,
                    # brackets, and curly braces) as actual indentation.
                    # For example:
                    # def foo():
                    #     "The spaces before this docstring are tokenize.INDENT"
                    #     test = [
                    #         "The spaces before this string do not get a token"
                    #     ]
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out

def reject(line):
    badwords = ["import"] #"input(", "print"]
    for badword in badwords:
        if badword in line:
            return True 
    return False 

def combine_one(code, main_body):
    # To do : Use import 
     
    with open(code, 'r') as f:
        lib = f.readlines()

    # lib = eval(remove_comments_and_docstrings(lib))

    newlines = [line for line in lib if not reject(line)]
    code = "".join(code.split())
    with open(code + ".cool", 'w') as f:
        f.writelines(newlines)
        f.write(main_body)
    return None 


import sys, token, tokenize
for code in glob.glob("hw3s/*3.py"):
    try:
        combine_one(code, main_body)
    except:
        print (code, "throw out. manual check ")

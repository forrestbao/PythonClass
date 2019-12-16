# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details. 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see http://www.gnu.org/licenses/.

# Copyleft 2019 Forrest Sheng Bao, Iowa State University 

# runs for Python 2 because Python3 has no StringIO 

import glob
# import StringIO, tokenize
import os, re

def substitute(line):
    patterns = ["import (?!random)",
                "\S+\.sort\(",
                "\S+\.remove\(",
                "\S+\.pop\(",
                "\S+\.index\(",
                "^(d(?!ef)|[a-c]|[e-h]|[j-z]|i(?!f))\w*",
#                "^\S+.*\(.*\)",
#                "print *\(.*\)"
#                "^(?!#).*"
            ]
    for pattern in patterns:
        x = re.search(pattern, line)
        if x != None:
            s, _ = x.span()
#            print "chaging", line[:-1], "to", line[:s] + "000"
            return line[:s] + "000\n"
    return line

def tweak_name(filename):
    filename = "".join(filename.split())
    filename = os.path.basename(filename)
    filename = filename[:-3] + "_grade.py" 
    return filename

def gen_header(filename):
    # filenmname: Some_body_hw3.py 
    filename = "".join(filename.split())    
    filename = os.path.basename(filename)
    headers = ""
#    headers += "msg=\"123\"\n"
    for func in "stairway, cycbrt, mypower, multiple, nbyn, alldivisor,  isperfect, triplecut, common_in_range, float2str, judge, user_moves, computer_moves, Uno".split(", "):
        header = "try:\n"
        header += "  from " + filename[:-3] + " import " + func + "\n"
        header += "except Exception as e:\n"
        header += "  print (e)\n"
        header += "  def {}(*args):\n".format(func)
        header += "    return None \n"
        # print (header)
        headers += header


    return headers

def gen_executable(student_library_filename, dstprefix, mainbody):
    headers = gen_header(student_library_filename)
    run_code_name = tweak_name(student_library_filename)
    run_code_path = os.path.join(dstprefix, run_code_name) 
    print "generating", run_code_path
    with open(run_code_path, 'w') as f:
        f.write(headers)
        f.write(mainbody)
    return run_code_path

def rewritefile(filename, dstprefix):  
    # the student module 
    # rewrite student submitted script 
    with open(filename, 'r') as f:
        lib = f.readlines()

    newlines = map(substitute, lib)
    filename = "".join(filename.split())
    # if "-" in filename:
    #     print filename
    filename = filename.replace("-", "_")
    filename = filename.replace("..", "_.")
    filename = os.path.basename(filename)
    
    (_, filename) = os.path.split(filename)

    filename  = os.path.join(dstprefix, filename)
    # print filename

    with open(filename, 'w') as f:

        headers = "from lib_hw5 import float2list, approxfloat, digit2char, integer2list\n"
        f.write(headers)
        f.writelines(newlines)
    return filename  


# gen_header("dafdsaf/sdafdsf.py")
# tweak_name("dafdsaf/sdafdsf.py")

if __name__ == "__main__":
    raw_submission_prefix = "hw5_submissions" # Places downloaded submissions, a bunch of .py files, here. 
    processed_student_script_prefix = "hw5_students" 


    with open("main_hw5.py", "r")  as f:
        main_body = f.read()

    import sys
    counter = 0 
    for code in glob.glob(raw_submission_prefix + "/*.py"):
        # try:
            student_library_filename = rewritefile(code, processed_student_script_prefix)
            gen_executable(student_library_filename, processed_student_script_prefix, main_body)
        # except:
        #     print (code, "throw out. manual check ")

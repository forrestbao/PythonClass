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





def grade_one_problem(your_function, my_function, data):
    try :
        your_result = list(itertools.starmap(your_function, data))
    except Exception as e:
        print (e)
        return False

    my_result = list(itertools.starmap(my_function, data))
    if len(my_result) != 0 and len(your_result)!= 0:
      return your_result == my_result 
    else:
      return False 


def grade_all_problems(your_functions, my_functions, datas, points, counter=0, verbose=False):
    grade = 0 
    correct = []
    if verbose:
      print ("correct problems: ", end="")
    for (yf, mf, data, pt) in zip(your_functions, my_functions, datas, points):
      print (yf.__name__, end=", ")
      if grade_one_problem(yf, mf, data):
        if verbose:
          print (counter, end=", ")
        correct.append(counter)
        grade += pt
      counter  += 1 
    if verbose:
      print (". Grade is", grade)
    return correct, grade 

if __name__ == "__main__":

    
    # import sys
    # banned_modules = ['math', 'cmath', 'statistics', 'numbers']
    # for module in banned_modules :
    # # for module in sys.modules:
    #   try :
    #     sys.modules[module]=None
    #   except:
    #     pass
 
    import random 
    import itertools
    import lib_hw3

    # map = itertools.starmap

    # test data for problems 2-5
    tax_data = random.choices(range(1, 2000, 10), k=10) # + [0, 49,50,51,99,100,101,499,499-50,501, 149,150,151,999,999-50, 999+50, 1000, 1000-50,1000+50, 1001-50, 1001+50, 1001]
    tax_data =  list(zip(tax_data)) 
    
    # test data for problem 6
    x = random.choices(range(0, 10000, 1), k=100)
    y = random.choices(range(0, 10000, 1), k=100)
    z = random.choices(range(0, 10000, 1), k=100)
    median_data = list(zip(x,y,z))

    # test data for problems 7 
    asciis = [chr(i) for i in range(32,126+1)]
    random.shuffle(asciis)
    # print (asciis)
    caesar_data = list(zip(asciis))
    # print ("".join(map(caesar_encoder, "Let's defeat the Germanic tribes")) )
    # print (list(map(lib_hw3.caesar_decoder, caesar_data)) )

    # test data for problem 8
    eq_data = median_data 
    
    # Pack everything 
    your_functions = [tax, tax2, tax3, median, caesar_encoder, caesar_decoder, solve_eq]
    my_functions = [lib_hw3.tax, lib_hw3.tax2, lib_hw3.tax3, lib_hw3.median, \
                   lib_hw3.caesar_encoder, lib_hw3.caesar_decoder, lib_hw3.solve_eq]
    datas = [tax_data, tax_data, tax_data, median_data, caesar_data, caesar_data, eq_data]
    points = [5,5,5,5, 5, 5,10]

    print (__file__, end=" ")
    correct, grade = grade_all_problems(your_functions, my_functions, datas, points, counter=3)
    # print (correct, grade)
    
    with open("grades.log", 'a+') as f:
      f.write(__file__)
      f.write("\t")
      x = " ".join(map(str,correct))
      f.write(",".join(map(str,correct)))
      f.write("\t ")
      f.write(str(grade))
      f.write("\n")

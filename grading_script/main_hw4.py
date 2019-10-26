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
      return your_result == my_result or your_result == (my_result)
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

    import random 
    import itertools
    import lib_hw4

    # map = itertools.starmap

    # test data 
    K = 10 
    ListofNumbers = random.choices(range(-K, K), k=2*K)+[0]
    ListofListsofNumbers = [random.choices(range(-K, K), k=2*K)+[0] for _ in range(K)]
    ListofPositiveIntegers = random.choices(range(1, 2*K), k=4*K)
    ListofRandomStrings = ["".join([chr(i) for i in random.choices(range(32, 127), k=K)]) for _ in range(K) ] 
    
    ZipListofListsofNumbers = list(zip(ListofListsofNumbers))
    ZipNumberListsandNumber = list(zip(ListofListsofNumbers, ListofNumbers))
    ZipTwoColumnPositiveIntegers = list(zip(ListofPositiveIntegers[:-2*K],ListofPositiveIntegers[2*K:]))
    ZipListofRandomStrings = list(zip(ListofRandomStrings))
    ZipListofPositiveIntegers = list(zip(ListofPositiveIntegers))
    
    # Pack everything 
    your_functions = [MaxPool, SilverMedal, BelongTo, gcd, PrintMe, Triangle, Typewriter, sift, Backward, BestApprox, SmallerApprox, BFF]
    my_functions = [lib_hw4.MaxPool, lib_hw4.SilverMedal, lib_hw4.BelongTo, lib_hw4.gcd, lib_hw4.PrintMe, lib_hw4.Triangle, lib_hw4.Typewriter, lib_hw4.sift, lib_hw4.Backward, lib_hw4.BestApprox, lib_hw4.SmallerApprox, lib_hw4.BFF]
    datas = [ZipListofListsofNumbers,  # maxpool
            ZipListofListsofNumbers,  # silvermedal
            ZipNumberListsandNumber,  # BelongTo
            ZipTwoColumnPositiveIntegers, # GCD
            ZipListofPositiveIntegers,   # PrintME
            ZipListofPositiveIntegers,   # Triangle 
            ZipListofRandomStrings,   # Typewriter
            ZipNumberListsandNumber,  # sift 
            ZipListofRandomStrings,   # Backward
            ZipNumberListsandNumber,  # BestApprox
            ZipNumberListsandNumber,  # SmallerApprox (bonus) 
            ZipListofListsofNumbers,  # BFF (bonus)
            ]
    points = [1,2,1,2,1, 1,1,1,1,2,1,3]
    #points = [p*40/58 for p in points]

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

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

def gen_judge_data(K):
    """generate K pairs of X's and O's
    """
    import random

    XOs= []


    for i in range(K):
        X, O = [[0 for _ in range(3)] for _ in range(3)], [[0 for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                t = random.choice([0,1,2,3,4]) #toss 
                if t == 0:
                    X[i][j] = 1
                elif t == 1:
                    O[i][j] = 1
                else:
                    pass


        mt = random.choice([0,1,2]) #mutations
        obj = random.choice([0,1]) # X wins or O wins 

        if obj == 0:
            P, Q = X, O 
        else:
            P, Q = O, X 

        if mt == 0: # row ones
            row = random.choice([0,1,2])
            P[row] = [1]*3
            Q[row] = [0]*3
        elif mt == 1: # column ones
            column = random.choice([0,1,2])
            for i in range(3):
                P[i][column] = 1
                Q[i][column] = 0
        else: # diagonal ones
            for i in range(3):
                P[i][i] = 1
                Q[i][i] = 0
        
        XOs.append((X,O))

    return XOs


if __name__ == "__main__":

    import random 
    import itertools
    import lib_hw5

    # map = itertools.starmap

    # test data 
    K = 10 

    ListofNumbers = random.choices(range(-K, K), k=2*K)+[0]
    ListofListsofNumbers = [random.choices(range(-K, K), k=2*K)+[0] for _ in range(K)]
    ListofPositiveIntegers = random.choices(range(1, K), k=2*K)
    ListofRandomStrings = ["".join([chr(i) for i in random.choices(range(32, 127), k=K)]) for _ in range(K) ] 
    ListofRandomReals = [random.uniform(1, 10000) for _ in range(K)]


    ZipListofListsofNumbers = list(zip(ListofListsofNumbers))
    ZipNumberListsandNumber = list(zip(ListofListsofNumbers, ListofNumbers))
    ZipTwoColumnPositiveIntegers = list(zip(ListofPositiveIntegers[:-K],ListofPositiveIntegers[K:]))
    ZipListofRandomStrings = list(zip(ListofRandomStrings))
    ZipListofPositiveIntegers = list(zip(ListofPositiveIntegers))

    
    precisions = [10**(-x) for x in range(10)] 
    cycbrt_data = list(zip( ListofRandomReals, random.choices(precisions, k=K)  ))
    power_data = list(zip(  ListofRandomReals, ListofPositiveIntegers ))

    judge_data = gen_judge_data(100) 

    uno_data = [ (x, x+y) for (x,y) in ZipTwoColumnPositiveIntegers  ]

    # Pack everything 
    your_functions = [stairway, cycbrt, mypower, multiple, nbyn, alldivisor, isperfect, triplecut, common_in_range, float2str, judge, Uno ]
    my_functions = [lib_hw5.stairway, lib_hw5.cycbrt, lib_hw5.mypower, lib_hw5.multiple, lib_hw5.nbyn, lib_hw5.alldivisor, lib_hw5.isperfect, lib_hw5.triplecut, lib_hw5.common_in_range, lib_hw5.float2str, lib_hw5.judge, lib_hw5.Uno  ]

    datas = [ZipListofPositiveIntegers,  # stairway
            cycbrt_data,  # cycbrt
            power_data,  # mypower
            ZipListofPositiveIntegers, # multiple 
            ZipListofPositiveIntegers, # nbyn
            ZipListofPositiveIntegers, # alldivisor
            ZipListofPositiveIntegers, # is_perfecty
            list(zip( random.choices(range(20, 100), k=K) ,  random.choices(range(1,5), k=K)  )), # triplecut
            ZipTwoColumnPositiveIntegers, # common_in_range 
            list(zip(ListofRandomReals+[0.1])), # float2str
            judge_data, # judge of tic-tac-toe  
            uno_data, # uno  
            ]

    points = [3,1,1,1,1, 
              1,1,1,2,1, 
              1,2,1,1,  
              1,  3] # judge and uno

    print (__file__, end=" ")
    correct, grade = grade_all_problems(your_functions, my_functions, datas, points, counter=1)

    grade += 2 # 2 free points for ko and cyrandom
    grade += 1 # one more free point for cycbrt

    # print (correct, grade)
    
    with open("grades.log", 'a+') as f:
      f.write(__file__)
      f.write("\t")
      x = " ".join(map(str,correct))
      f.write(",".join(map(str,correct)))
      f.write("\t ")
      f.write(str(grade))
      f.write("\n")

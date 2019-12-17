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
    import caesar

    # test data 
    K = 10 


    RandomASCIIs = [random.choices(range(48, 122+1), k=K) for _ in range(K)]
    RandomStrings =  ["".join(map(chr, random.choices(range(48,122), k=K))) for _ in range(K) ]

    RandomChars = list(map(chr, random.choices(range(48, 122+1), k=K))) 
    Random26s =  random.choices(range(1,26), k=K) 
    
    EnglishWords = caesar.load_english("english.txt")
    RandomWords = [random.choices(EnglishWords, k = K) + RandomStrings  for _ in range(K)]
    [random.shuffle(x) for x in RandomWords] # in-place shuffle
    # list of lists of (words and gebbrish)
    

    # Pack everything 
    your_functions = [ascii2string, string2ascii, encrypt1, decrypt1, encrypt_string, decrypt_string, load_english, check_legit, crack]
    my_functions = [caesar.ascii2string, caesar.string2ascii, caesar.encrypt1, caesar.decrypt1, caesar.encrypt_string, caesar.decrypt_string, caesar.load_english, caesar.check_legit, caesar.crack]


    datas = [list(zip(RandomASCIIs)),  # ascii2string
             list(zip(RandomStrings)), # string2ascii
             list(zip(RandomChars, Random26s)),  # encrypt1
             list(zip(RandomChars, Random26s)),  # decrypt1
             list(zip(RandomStrings, Random26s)) , # encrypt_string
             list(zip(RandomStrings, Random26s)) , # decrypt_string
             list(zip(["english.txt"]*K)),  # load_english
             list(zip(RandomWords, EnglishWords*K)), # check_legit
             list(zip( [" ".join(x) for x in RandomWords], ["english.txt"]*K))  # crack
            ]


    points = [1,1,2,2,3,
              3,2,2,4]

    print (__file__, end=" ")
    correct, grade = grade_all_problems(your_functions, my_functions, datas, points, counter=1)


#    print (correct, grade)
    
    with open("grades.log", 'a+') as f:
      f.write(__file__)
      f.write("\t")
      x = " ".join(map(str,correct))
      f.write(",".join(map(str,correct)))
      f.write("\t ")
      f.write(str(grade))
      f.write("\n")

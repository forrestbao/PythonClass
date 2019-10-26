
rm grades.log
rm hw4_students/* 
cp lib_hw4.py hw4_students

python combine.py

#exit 8

for i in hw4_students/*_grade.py
do 
echo -n "grading ... "
#echo -n $i 
echo -n "   "
python3  $i #2> /dev/null
echo " " 
echo " "
done


rm grades.log
rm hw3_students/* 
cp lib_hw3.py hw3_students

python combine.py

#exit 8

for i in hw3_students/*_grade.py
do 
echo -n "grading ... "
#echo -n $i 
echo -n "   "
python3  $i #2> /dev/null
echo " " 
echo " "
done


rm grades.log
rm hw5_students/* -rf 
cp lib_hw5.py hw5_students

python combine.py

#exit 8

for i in hw5_students/*_grade.py
do 
echo -n "grading ... "
#echo -n $i 
echo -n "   "
python3  $i #2> /dev/null
echo " " 
echo " "
done

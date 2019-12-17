
rm grades.log
rm hw6_students/* -rf 
cp caesar.py hw6_students

python combine.py

#exit 8

for i in hw6_students/*_grade.py
do 
echo -n "grading ... "
#echo -n $i 
echo -n "   "
python3  $i #2> /dev/null
echo " " 
echo " "
done

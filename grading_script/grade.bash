
python combine.py

rm hw3s/lib_hw3.py.cool

for i in hw3s/*.py.cool
do 
echo -n "grading ... "
echo -n $i 
echo -n "   "
python3  $i #2> /dev/null
echo " " 
done

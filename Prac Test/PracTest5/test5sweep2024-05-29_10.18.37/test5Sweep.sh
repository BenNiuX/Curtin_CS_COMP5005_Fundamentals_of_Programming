#!/bin/bash

exp_dir=test5sweep`date "+%Y-%m-%d_%H.%M.%S"`
mkdir $exp_dir

cp test5.py $exp_dir
cp test5Sweep.sh $exp_dir
cd $exp_dir
low_r=$1
hi_r=$2
step_r=$3
low_a=$4
hi_a=$5
step_a=$6

echo "Parameters are: "
echo "R values : " $low_r $hi_r $step_r
echo "A values : " $low_a $hi_a $step_a

for r in `seq $low_r $step_r $hi_r`;
do
    for a in `seq $low_a $step_a $hi_a`;
    do
        echo "Experiment: " $r $a
        # echo "Change this line to run test5.py with parameters"
        # bash test5Sweep.sh 0.00210 0.00220 0.00001 0.3 0.6 0.1
        python3 test5.py $r $a
    done
done
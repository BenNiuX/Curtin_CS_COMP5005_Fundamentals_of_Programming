#!/bin/bash

year=$1
month=$2

exp_dir=plot_"$year"_"$month"
echo $exp_dir
mkdir $exp_dir
cp weather_workflow.sh $exp_dir 
cp plotcmd.txt $exp_dir 
cd $exp_dir

echo "Parameters are: "
echo "Year : " $year
echo "Month : " $month

header='--header=User-Agent: Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'
wget "$header" http://www.bom.gov.au/climate/dwo/"$year""$month"/text/IDCJDW6111."$year""$month".csv
grep "$year"-"$month"- IDCJDW6111."$year""$month".csv > data.csv
awk -F "," '{print $3, $4, $11, $17}'  data.csv > data4.csv
echo "plot for [col=1:4] './data4.csv' using 0:col with lines" > plotcmd.txt
# gnuplot -p  plotcmd.txt
gnuplot -e "set terminal png size 400,300; set output '$year$month.png'; plot for [col=1:4] './data4.csv' using 0:col with lines"


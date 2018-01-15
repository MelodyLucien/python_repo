#!/bin/bash

filename=$1

if [ -z $filename ];then
  exit 0
fi

if [ ! -e filenumber.txt ];then
    echo 1 > filenumber.txt
fi

num=`cat filenumber.txt`

touch $num.$filename.py

echo "#!/usr/bin/python3" > $num.$filename.py

chmod 777 $num.$filename.py

echo $(( num + 1 )) > filenumber.txt



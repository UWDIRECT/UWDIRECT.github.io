#!/bin/bash


echo "making directory"
mkdir HCEPDB

echo "changing directory"
cd HCEPDB

echo "This is the README" > README.txt

echo "downloading file"
curl http://faculty.washington.edu/dacb/HCEPDB_moldata.zip -o HCEPDB_moldata.zip

echo "unzipping file"
unzip HCEPDB_moldata.zip

echo "dumping the first few lines of the file"
head -2 HCEPDB_moldata.csv

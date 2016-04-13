# This script is used to take a Wireshark capture in CSV format
# strip all lines except for the ones with SYN, then strip  all columns
# except src IP, dst IP, protocol and info
# It requires you to store the data in a file named cap.csv
# change the directory to where the file is stored.

import csv
import os

directory = 'C:\Python27\Scripts'
os.chdir(directory)

def create_column_headings():
    with open("cap.csv", 'rb') as f:
        for line in f:
            if 'No.' in line:
                with open("cap_SYN.csv", "a") as myfile:
                    #l = line.strip()
                    myfile.writelines(line)

def collect_SYN():
    with open("cap.csv", 'rb') as f:
        for line in f:
            if '[SYN]' in line:
               #print line
               with open("cap_SYN.csv", "a") as myfile:
                   l = line.strip()
                   myfile.writelines(l)
                   myfile.writelines('\n')

def strip_columns():
    with open('cap_SYN.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        #for row in reader:
        for row in reader:
            print(row['Source'], row['Destination'], row['Protocol'], row['Info'])

create_column_headings()
collect_SYN()
strip_columns()

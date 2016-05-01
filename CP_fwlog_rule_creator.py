import os
import csv

directory = 'C:\Python27\my_scripts'
os.chdir(directory)

file = "sgsgvoges002.2015-09-27_001827_732.log.txt"
file2 = "sgsgvoges002.2015-09-27_001827_732.log.txt"
file3 = 'CP_FW_log1.csv'
file4 = 'CP_FW_log1_row_strip.csv'
file5 = 'CP_FW_log1_unique.csv'

print directory

def line_count(x):
    a = 0
    #if a < 6:
    with open(x, 'rb') as f:
        for line in f:
            a = a + 1
    print a

def preview_file():
    a = 0
    # if a < 6:
    with open(file, 'rb') as f:
        for line in f:
            a = a + 1
            if a < 6:
               print line.strip()
			   
def delete_working_files():
    try:
         os.remove ('CP_FW_log1.csv')
    except:
	    pass
    try:
         os.remove ('file3-comma.txt')
    except:
	    pass
    try:
         os.remove ('CP_FW_log1_unique.csv')
    except:
	    pass
    try:
         os.remove ('CP_FW_log1_row_strip.csv')
    except:
	    pass
		

def convert_semicolon_to_comma():
    a = ('\n')
    f1 = open(file2, 'r')
    f2 = open('file3-comma.txt', 'a')
    for line in f1:
       f2.write(line.replace(';', ','))
    f1.close()
    f2.close()

def add_headings_to_csv():
    with open('CP_FW_log1.csv', 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Date time accept-deny fw name", "Interface-Service ID", "source", "destination", "protocol", "rule", "product", "service", "source port", "product_family"])					

def import_fwlog_in_csv():
    with open('file3-comma.txt', 'rb') as f:
        for line in f:
            with open("CP_FW_log1.csv", "a") as myfile:
                if 'accept' in line:
                    l = line.strip()
                    myfile.writelines(l+'\n')

def strip_columns():
    with open(str(file3)) as csvfile:
        reader = csv.DictReader(csvfile)
        with open(file4, "a") as myfile:
            for row in reader:
                a = (row['source'], row['destination'], row['service'])
                myfile.write (str(a)+"\n")

			
def unique_rows():
    with open(file4,'r') as in_file, open(file5,'w') as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen: continue # skip duplicate
            seen.add(line)
            out_file.write(line)
			

#line_count()
#preview_file()
delete_working_files()
convert_semicolon_to_comma()
add_headings_to_csv()
import_fwlog_in_csv()
strip_columns()
unique_rows()
line_count(file2)
line_count(file5)

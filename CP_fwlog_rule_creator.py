import os
import csv

directory = 'C:\Python27\my_scripts'
os.chdir(directory)

file  = "sgsgvoges002.2015-09-27_001827_732.log.txt"
file_tmp = "TEMP.log.txt"
file1 = "sgsgvoges002.2015-09-27_001827_732-EDITED.log.txt"
file2 = "CP_FW_log1_header.csv"
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

def preview_file(x):
    a = 0
    # if a < 6:
    with open(x, 'rb') as f:
        for line in f:
            a = a + 1
            if a < 6:
               print line.strip()
			   
def preview_file2(x):
    a = 0
    # if a < 6:
    with open(x, 'rb') as f:
        for line in f:
            a = a + 1
            if a < 60000000:
                if 's_port: 59939' in line:
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
		

def clean_file():
    a = ('\n')
    f1 = open(file, 'r')
    f2 = open(file_tmp, 'w')
    for line in f1:
       f2.write(line.replace('; src', ' src'))
    f1.close()
    f2.close()
    f1 = open(file_tmp, 'r')
    f2 = open(file1, 'w')
    for line in f1:
       f2.write(line.replace(' src', '; src'))
    f1.close()
    f2.close()
    try:
        os.remove ('TEMP.log.txt')
    except:
	    pass

def add_headings_to_csv():
    with open(file2, 'wb') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["Date time accept-deny fw name Interface-Service ID", "source", "destination", "protocol", "rule", "product", "service", "source port", "product_family"])					

def convert_comma_to_semicolon():
    a = ('\n')
    f1 = open(file2, 'r')
    f2 = open(file3, 'w')
    for line in f1:
       f2.write(line.replace(',', ';'))
    f1.close()
    f2.close()

def import_fwlog_in_csv():
    with open(file1, 'rb') as f:
        for line in f:
            with open(file3, "a") as myfile:
                if 'accept CN=AUSYZVFOGES002_AUSYZFVOGES005' in line:
                    l = line.strip()
                    myfile.writelines(l+'\n')

def remove_comma():
    a = ('\n')
    f1 = open(file2, 'r')
    f2 = open(file3, 'w')
    for line in f1:
       f2.write(line.replace(',', ';'))
    f1.close()
    f2.close()

def strip_columns():
    with open(str(file3)) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        with open(file4, "a") as myfile:
            for row in reader:
                a = (row['source'], row['destination'], row['protocol'], row['service'])
                myfile.write (str(a)+"\n")

			
def unique_rows():
    with open(file4,'r') as in_file, open(file5,'w') as out_file:
        seen = set() 
        for line in in_file:
            if line in seen: continue 
            out_file.write(line)
			

#line_count()
#preview_file('file3-comma.txt')
#preview_file2('file3-comma.txt')
delete_working_files()
clean_file()
add_headings_to_csv()
convert_comma_to_semicolon()
import_fwlog_in_csv()
strip_columns()
unique_rows()
line_count(file2)
line_count(file5)


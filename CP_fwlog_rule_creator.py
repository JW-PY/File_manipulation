import os
import csv

directory = 'C:\Python27\my_scripts'
os.chdir(directory)

file = "sgsgvoges002.2015-09-27_001827_732.log.txt"
file2 = "test_log.txt"

print directory

def line_count():
    a = 0
    #if a < 6:
    with open(file, 'rb') as f:
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
    file3 = 'CP_FW_log1.csv'
    with open(str(file3)) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['source'], row['destination'], row['service'])
			
			

#line_count()
#preview_file()
delete_working_files()
convert_semicolon_to_comma()
add_headings_to_csv()
import_fwlog_in_csv()
strip_columns()

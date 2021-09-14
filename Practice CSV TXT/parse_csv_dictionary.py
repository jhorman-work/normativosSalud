import csv
import os

current_path = os.path.dirname(__file__)

csv_file_path = current_path + '\\names.csv'
with open(csv_file_path, mode='r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    new_csv_file_path = current_path + '\\new names.csv'
    with open(new_csv_file_path, 'w', newline = '') as new_file:
        field_names = ['first_name', 'last_name', 'email'] # with DictWriter you need to provide the headers
        csv_writer = csv.DictWriter(new_file, fieldnames = field_names, delimiter='\t')
        
        csv_writer.writeheader() # writes the headers, the first line in new_file
        
        for line in csv_reader:
            csv_writer.writerow(line)

        # if you don't want to print a field, don't include it in the field_names
        # and use del inside the printing loop to del that line
"""         for line in csv_reader:
            del line['email']
            csv_writer.writerow(line) """

        # with DictReader is easier to parse
"""     for line in csv_reader:
        print(line['email']) """
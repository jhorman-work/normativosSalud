import csv
import os

current_path = os.path.dirname(__file__)
csv_file_path = current_path + '\\names.csv'

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file) # second argument is delimiter, default is ,
    
    new_csv_file_path = current_path + '\\new names.csv'
    with open(new_csv_file_path, 'w', newline = '') as new_file: # open creates a new file if it doesn't exist
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)
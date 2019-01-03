import csv

def manipulate_rows(file_to_manipulate,row_to_manipulate, new_data):
        '''
        Function that manipulated the already existing data in 
        a given row in the csv file
        '''

        # the new data variable should be given in the form of a
        # list of items
        row = new_data

        with open(file_to_manipulate, 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[row_to_manipulate] = row

        with open(file_to_manipulate, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)

        readFile.close()
        writeFile.close()

def appending_new_rows(file_to_manipulate,new_data):
        '''
        Function that appends collected data as a new row in the 
        the given file
        '''
        
        # the new data variable should be given in the form of a
        # list of items
        row = new_data

        with open(file_to_manipulate, 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
        csvFile.close()




# the secion below contains functions for test purposes only
my_file = "details.csv"
data = [1,2,3]


def read_csv_file(file_to_manipulate, data_to_write):
        my_data = [1,2,3]

        with open(file_to_manipulate) as csv_file:

                # reading from csv
                csv_reader = csv.reader(csv_file, delimiter = ",")
                line_count = 0

                for row in csv_reader:
                        if line_count == 0:
                                print("Column names are :"+ str(row))
                                line_count += 1

                        else:
                                print(row)
                                line_count += 1

def write_csv_file(file_to_manipulate):   
        with open(file_to_manipulate, mode='w') as csv_file:
                # writting to file
                csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([4,5,6])
                csv_writer.writerow([7,8,9])

        csv_file.close()




# manipulate_csv_file(my_file,data)
# write_csv_file(my_file)
# manipulate_rows(my_file,1,[1,2,3])
# appending_new_rows(my_file,[1,2,3])
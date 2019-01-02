import csv


def write_to_file():
    my_data = [1,2,3]

    my_file = open('details.csv','w')

    with my_file:
        writer = csv.writer(my_file)
        writer.writerow(my_data)

write_to_file()
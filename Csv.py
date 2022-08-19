import csv

list1 = ['Name', 'Branch', 'Year', 'CGPA'] #create two lists
list2 = [ ['Shoaib', 'CSE', '2', '9.6'],
        ['Rohit', 'CSE', '2', '9.58']]

file = "File.csv"   #creating a file name and assigning to variable
with open(file, 'w') as csvfile:     # open the file in write mode as csVfile(some variable)
    write = csv.writer(csvfile)      # variable = csv.writer(variable)
    write.writerow(list1)
    write.writerows(list2)

csv.reader(file)


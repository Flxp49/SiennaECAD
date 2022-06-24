import csv
files = []

def processCompare(file):
    with open(file, mode ='r') as f:
        next(f)
        csvFile = csv.reader(f)
        for lines in csvFile:
            print(lines)
            

n = int(input("Enter the no files to compare: "))
for i in range(n):
    files.append(input("Enter filename" + str(i+1)+": "))
for file in files:
    processCompare(file)
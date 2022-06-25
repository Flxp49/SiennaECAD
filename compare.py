import csv
import pandas as pd
files = []
data = []
match = []
mismatch = []

def process(file):
    fileData = []
    with open(file, mode ='r') as f:
        csvFile = csv.reader(f)
        next(f)
        for line in csvFile:
            fileData.append(line)
    f.close()
    data.append(fileData)

def compare():
    m = 0
    for cmp in data[0]: 
        for j in data[1]:
            if cmp[0] == j[0] and cmp[1] == j[1]:
                match.append(cmp)
                m = 1
                break
        if (m != 1):
            mismatch.append(cmp)
    print(len(match))
    print(len(mismatch))
    pd.DataFrame(match, columns=['column_one', 'column_two']).to_csv("Match.csv")
    pd.DataFrame(mismatch, columns=['column_one', 'column_two']).drop_duplicates(keep=False).to_csv("Mismatch.csv")


def main():     
    # n = int(input("Enter the no of files to compare: "))
    # if n>1:
    n=2
    for i in range(n):
        files.append(input("Enter filename" + str(i+1)+": "))
    for file in files:
        process(file)
    compare()
    # else:
        # print("Please enter >1")
main()
import os
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
    for cmp in data[0]: 
        m = 0
        for j in data[1]:
            if cmp[0] == j[0] and cmp[1] == j[1]:
                match.append(cmp)
                m = 1
                break
        if (m != 1):
            mismatch.append(cmp)
    for cmp in data[1]: 
        m = 0
        for j in data[0]:
            if cmp[0] == j[0] and cmp[1] == j[1]:
                match.append(cmp)
                m = 1
                break
        if (m != 1):
            mismatch.append(cmp)
    print(len(match))
    print(len(mismatch))
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Compare')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    pd.DataFrame(match, columns=['Net Name', 'Component Name']).drop_duplicates(keep=False).to_csv("Compare/Match.csv")
    pd.DataFrame(mismatch, columns=['Net Name', 'Component Name']).drop_duplicates(keep=False).to_csv("Compare/Mismatch.csv")


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
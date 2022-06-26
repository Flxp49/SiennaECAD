import os
import pandas as pd
files = []

# Allegro_netlist-f.csv
# DX-Netlist-f.csv

def compare():
    df1 = pd.read_csv(files[0])
    df2 = pd.read_csv(files[1])
    df1 = pd.concat([df1, df2])
    print(df1)
    mdf = df1[df1.duplicated("Component Name", keep=False)].drop_duplicates(keep="first")
    print(mdf)
    misdf = pd.concat([df1, mdf]).drop_duplicates(keep=False)
    print(misdf)
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Compare')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    mdf.to_csv("Compare/Match.csv")
    misdf.to_csv("Compare/Mismatch.csv")
    # verify(mdf, misdf, df1)

# def verify(d1, d2, d):
#     d1 = pd.concat([d1,d2]).drop_duplicates(keep=False)
#     print(d1)
#     print(d.drop_duplicates())



def main():     
    # n = int(input("Enter the no of files to compare: "))
    # if n>1:
    n=2
    for i in range(n):
        files.append(input("Enter filename" + str(i+1)+": "))
    compare()
    # else:
        # print("Please enter >1")
main()
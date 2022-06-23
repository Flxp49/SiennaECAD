import csv
import xlrd
files = []


def createFormattedFile(data, filename):
    filename = (filename.split(".")[0]+"-f.csv")
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['column_one', 'column_two']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

    print("Data written to", filename)


def processNet(filename):
    original_data = list()
    final_data = list()
    column_one = ""
    column_two = ""
    c = 0
    with open(filename, "r") as file:
        for line in file.readlines():
            if line.strip() != "":
                original_data.append(line.strip())

        for i in range(0, len(original_data)):
            if original_data[i] not in ["[", "]", "(", ")"] and c == 0:
                column_one = original_data[i]
                c = c+1
            elif original_data[i] not in ["[", "]", "(", ")"] and c != 0:
                column_two = original_data[i]
                temp_dict = {
                    "column_one": column_one,
                    "column_two": column_two
                }
                final_data.append(temp_dict)
            else:
                c = 0
                
    createFormattedFile(final_data, filename)
    

def processXls(filename):
    type = int(input("Enter the type of xls file for " + str(filename) + ", 1: Cadence OR 2: Xpedition: "))
    final_data = list()
    column_one = ""
    column_two = ""
    if type == 1:
        wb = xlrd.open_workbook(filename)
        sheet = wb.sheet_by_index(0)
        for i in range(3, sheet.nrows):
            column_one = sheet.cell_value(i, 0)
            cmps = sheet.cell_value(i, 1).split()
            for j in cmps:
                column_two = j
                temp_dict = {
                    "column_one": column_one,
                    "column_two": column_two
                }
                final_data.append(temp_dict)

    elif type == 2:
        wb = xlrd.open_workbook(filename)
        sheet = wb.sheet_by_index(0)
        for i in range(3, sheet.nrows):
            if (sheet.cell_value(i, 0) != ""):
                column_one = sheet.cell_value(i, 0)
                continue
            elif (sheet.cell_value(i, 0) == "" and sheet.cell_value(i, 3) == ""):
                continue
            elif (sheet.cell_value(i, 0) == ""):
                column_two = sheet.cell_value(i, 3)
                temp_dict = {
                    "column_one": column_one,
                    "column_two": column_two
                }
                final_data.append(temp_dict)
    else:
        print("Invalid input, Please enter 1 or 2")
        return

    createFormattedFile(final_data, filename)

def processText(filename):
    original_data = list()
    with open(filename, "r") as File:
        for line in File.readlines():
            temp_list = line.split()
            if temp_list != []:
                original_data.append(line.split())

    # Find out what type text file it is
    textTypeloc = getTextType(original_data)
    if textTypeloc[0] == 1:
        cdata = original_data[textTypeloc[1]:-1]
        fdata = getMappings(cdata, textTypeloc[0])
    elif textTypeloc[0] == 2:
        cdata = original_data[textTypeloc[1]:-1]
        fdata = getMappings(cdata, textTypeloc[0])
    else:
        print("ERROR, TextType unknown.")
        return

    createFormattedFile(fdata, filename)


def getTextType(data):
    for i in range(len(data)):
        if ".ADD_TER" in data[i]:
            return 1, i
        elif "*" in data[i][0]:
            return 2, i
    return -1, -1


def getMappings(data, type):
    final_data = list()
    column_one = ""
    column_two = ""

    if type == 1:
        for i in data:
            # Updating column one if the row is .ADD_TER
            if ".ADD_TER" in i:
                column_one = i[3]
                column_two = i[1] + i[2]

            # Updating the column two details
            elif ".TER" in i:
                column_two = i[1] + i[2]
            else:
                column_two = i[0] + i[1]

            temp_dict = {
                "column_one": column_one,
                "column_two": column_two
            }
            final_data.append(temp_dict)
        return final_data

    elif type == 2:
        for i in data:
            # Updating column one if the row is *
            if "*" in i[0]:
                column_one = i[0] + " " + i[1]
            else:
                for j in i:
                    column_two = j
                    temp_dict = {
                        "column_one": column_one,
                        "column_two": column_two
                    }
                    final_data.append(temp_dict)
        return final_data


n = int(input("Enter the no files to convert: "))
for i in range(n):
    files.append(input("Enter filename" + str(i+1)+": "))
for file in files:
    fileformat = file.split(".")[1]
    if fileformat == "txt":
        processText(file)
    elif fileformat == "xls":
        processXls(file)
    elif fileformat == "net":
        processNet(file)

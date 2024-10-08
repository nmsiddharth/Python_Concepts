import csv

data = open("E:\\SIDDU\\Technical\\Python\\Complete-Python-3-Bootcamp-master\\15-PDFs-and-Spreadsheets\\example.csv",encoding='utf-8')

csv_data = csv.reader(data)

data_lines = list(csv_data)
print(data_lines[10][2])

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)



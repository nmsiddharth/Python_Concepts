import csv

data = open("new_csv.csv",mode="w",newline='')

data_writer = csv.writer(data,delimiter=',')

data_writer.writerows([['1','2','3'],['4','5','6']])

data.close()

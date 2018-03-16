

import csv
import os

stocks = []
path = "/Users/luyang/PycharmProjects/cpmputationalFinance/stocks"
files= os.listdir(path)
for i in range(len(files)):
    # print os.path.splitext(files[i])[0]
    if os.path.splitext(files[i])[1] == '.csv':
        filename = os.path.splitext(files[i])[0]
        # print filename
        stocks.append(filename)
print(files)
print(stocks)

# stocks = files
all = []
# dic = dict.fromkeys(stocks)
# print("/Users/luyang/PycharmProjects/test/stocks/"+stocks[1]+".csv")
for i in range(len(stocks)):
    with open("/Users/luyang/PycharmProjects/cpmputationalFinance/stocks/"+stocks[i]+".csv","rb") as csvfile:
        reader = csv.reader(csvfile)
        column = [row[4] for row in reader]
        print(column)
        column = column[1:]
        print(column)
        # column = list(map(lambda x:float(x), column))
        # print(column)
        column.insert(0, stocks[i])
        # for j in range(len(column)):
        #     dic[stocks[i]][j] = column[j]
        # print dic
        all.append(column[0:])

print("all")
print(all)

# rows = zip(all[0])
# for i in len(row)
# print(rows)
with open("/Users/luyang/PycharmProjects/cpmputationalFinance/stocks/teststocks.csv", "w") as csvfile:
        # fieldnames = stocks
        writer = csv.writer(csvfile)

        # writer.writeheader()
        # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        # writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        # writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        # for i in range(len(stocks)):
        for j in all:
            writer.writerow(j)

# column to row
# def col_selector(table,column_key):
#     return [row[column_key] for row in table]
# with open('./test.csv','rb') as f:
#     reader1 = csv.reader(f,delimiter=',')
#     table1 = [row for row in reader1]
#     for var in range(0,756):
#         col = col_selector(table1,var)
#         outputdata = open('./teststocks.csv','ab')
#         writer1 = csv.writer(outputdata)
#         writer1.writerow(col)
#         outputdata.close()


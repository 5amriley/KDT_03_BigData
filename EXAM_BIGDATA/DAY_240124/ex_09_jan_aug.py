import csv
import matplotlib.pyplot as plt

filename = '../DATA/daegu-utf8.csv'
f = open(filename, encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data:
    if row[-1] != '':
        month = row[0].split('-')[1]
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))
f.close()

plt.hist(aug, bins=100, color='tomato', label='Aug')
plt.hist(jan, bins=100, color='b', label='Jan')
plt.xlabel('Temperature')
plt.rc('axes', unicode_minus=False)

plt.legend()
plt.show()

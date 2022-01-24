import csv
with open('height-weight.csv', newline = '') as f:
    r1 = csv.reader(f)
    file_data = list(r1)
file_data.pop(0)
new_data = []
for i in range (len (file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
n = len(new_data)
total = 0
for u in new_data:
    total += u
mean = total/n
print("The mean of the total value is: ", str(mean))    
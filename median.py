import csv
from statistics import median

from numpy import average
with open("hw.csv", newline = "") as f:
   reader = csv.reader(f)
   file_data = list ( reader)

file_data.pop(0)
 #hw data to get the hight and weight
new_data = []
for i in range(len(file_data)):
        n_sum = file_data[i] [i]
        new_data.append(float)(n_sum)

# getting the median
n = len(new_data)
new_data.sort()

# 

if  n%2 ==0:

    median1 = float(new_data[n//2])

    median2 = float(new_data[n//2-1])
    median = (median1+ median2)/2

else: 
    median = new_data(n//2)
print(0)
print("medin is : " + str(median))
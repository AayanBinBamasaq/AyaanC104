import csv

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

#getting the sum
n =len(new_data)
total =0
for x in new_data:
    total +=x

    mean = total/n
    print ("mean/average Is:"  + str(mean))
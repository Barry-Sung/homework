# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
# Part. 2
#=======================================
# Read cwb weather data

cwb_filename = '107061271.csv'

data = []

header = []

with open(cwb_filename) as csvfile:

   mycsv = csv.DictReader(csvfile)

   header = mycsv.fieldnames

   for row in mycsv:

      data.append(row)

#=======================================
# Part. 3

#=======================================

# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.

#target_data = data[:10]


#=======================================


# Part. 4

#=======================================

# Print result
a = []
b = []
for i in range(len(data)): 
   a.append(data[i]['station_id'])
   b.append(data[i]['HUMD'])

   
for p in range(len(data)):
   if float(b[p])==-99.000 or float(b[p])==-999.000:
      a[p]='0'
      b[p]='0'


sum1=0
for j in range(len(a)):
   if a[j]=='C0A880':
      sum1 = sum1 + float(b[j])
sum2=0
for k in range(len(a)):
   if a[k]=='C0F9A0':
      sum2 = sum2 + float(b[k])
sum3=0
for l in range(len(a)):
   if a[l]=='C0G640':
      sum3 = sum3 + float(b[l])
sum4=0
for m in range(len(a)):
   if a[m]=='C0R190':
      sum4 = sum4 + float(b[m])
sum5=0
for n in range(len(a)):
   if a[n]=='C0X260':
      sum5 = sum5 + float(b[n])

d = {'C0A880':str(sum1),'C0F9A0':str(sum2),'C0G640':str(sum3),'C0R190':str(sum4),'C0X260':str(sum5)}

print(d)


#========================================

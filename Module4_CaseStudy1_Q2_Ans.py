import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
# arr = np.genfromtxt(path_to_csv, dtype=None, delimiter=',', skip_header=1)
arr = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
# print arr
count_of_phd=0
temp=0
for i in range(len(arr)):
    temp = int(arr[i][3])
    if temp==1:
        count_of_phd=count_of_phd+temp

print count_of_phd
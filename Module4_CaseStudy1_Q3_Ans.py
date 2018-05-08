import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
arr = np.loadtxt(path_to_csv, dtype=np.object, delimiter=",", skiprows=1)
for i in range(len(arr)):
    print arr[i][2]
# Extract data from the given CSV file and store the data from each column in a separate NumPy array

import numpy as np
path_to_csv='c:\\temp\\SalaryGender.csv'
data = np.genfromtxt(path_to_csv, dtype=None, delimiter=',', skip_header=1)
print data
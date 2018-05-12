import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['Month','Amount']]
x=np.array(selected_data['Month'])
y=np.array(selected_data['Amount'])
plt.scatter(x,y)
plt.xlabel('Month of Sales')
plt.ylabel('Total Amount of Sales')
plt.grid()
plt.show()


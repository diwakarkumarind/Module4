#Plot Total Sales Per Month for Year 2011. Bar chart
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['Month','Quantity']]
x=np.array(selected_data['Month'])
y=np.array(selected_data['Quantity'])
plt.bar(x,y)
plt.xlabel('Month of Sales')
plt.ylabel('Total Sales')
plt.grid()
plt.savefig('C:\\Users\\Diwakar\\Pictures\\TotalSales2011_Bar.png')
plt.show()

# Bar Chart isn't the better choice to visualize than Simple Plot
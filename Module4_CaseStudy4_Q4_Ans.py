# Plot Scatter Plot for the invoice amounts and see the concentration of amount.
# In which range most of the invoice amounts are concentrated
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("c:\\temp\\BigMartSalesData.csv")
selected_data=dataset.loc[:,['InvoiceNo','Amount']]
x=np.array(selected_data['InvoiceNo'])
y=np.array(selected_data['Amount'])
plt.scatter(x,y)
plt.xlabel('Invoice No')
plt.ylabel('Amount')
plt.grid()
plt.savefig('C:\\Users\\Diwakar\\Pictures\\TotalSales2011_scatter.png')
plt.show()

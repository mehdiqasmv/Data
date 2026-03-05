import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data={
    'Product':['Keyboard','Mouse','Laptop','Headphone','Phone'],
    'Sales':[123,145,80,201,143]
}

df=pd.DataFrame(data)


plt.figure(figsize=(10,8))

sns.barplot(x='Product',y='Sales',data=df,palette='viridis')

plt.title('Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')


plt.show()


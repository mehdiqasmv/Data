import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data ={
    'Product':['Keyboard','Mouse','Laptop'],
    'Sales':[110,104,89]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10,6))

sns.barplot(x='Product', y='Sales', data=df,palette='viridis')

plt.title('Product Sales')
plt.xlabel('Product')
plt.ylabel('Sales AZN')

plt.show()
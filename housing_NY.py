# housing_NY.py
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('FMAC-HPI_NY.xls', 
                   'Worksheet1', index_col=0)
print(df.head(3))

df.plot()
plt.show()

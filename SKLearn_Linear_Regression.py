import numpy as np

# buat data jumlah kamar
bedrooms = np.array([1,1,2,2,3,4,4,5,5,5])

# data harga rummah. asumsi dalam dollar
house_price = np.array([15000, 18000, 27000, 34000, 50000, 68000, 65000, 81000,85000, 90000])

# menampilkan scatter plot dari dataset
import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(bedrooms, house_price)

from sklearn.linear_model import LinearRegression

# latih model dengan Linear Regression.fit()
bedrooms = bedrooms.reshape(-1, 1)
print(bedrooms)
linreg = LinearRegression()
linreg.fit(bedrooms, house_price)

# menampilkan plot hubungan antara jumlah kamar dan harga rumah
plt.scatter(bedrooms, house_price)
plt.plot(bedrooms, linreg.predict(bedrooms))


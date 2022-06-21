import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import stats
import pandas
import math
from sklearn import linear_model


speed = [32,111,138,28,59,77,97]

standard_dev = numpy.std(speed)
var = numpy.var(speed)
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 23)

print(x)
print(standard_dev)
print(pow(standard_dev, 2))
print(var)
"""
x = numpy.random.normal()
    (5.0, 1.0, 100000)
"""
plt.hist(x, 100)
plt.show()

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2, 1000)

plt.scatter(x, y)
plt.show()

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)

speed = myfunc(10)
print(speed)


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

speed = mymodel(17)

print(r2_score(y, mymodel(x)))
print(speed)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()


df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)



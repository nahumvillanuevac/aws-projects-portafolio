"REGRESIÓN LINEAL"

from sklearn.linear_model import LinearRegression

x = [[1], [2], [3], [4], [5], [6]]
y = [1, 3, 5, 7, 9, 10]

modelo = LinearRegression()
modelo.fit(x, y)

print(modelo.predict([[4]]))

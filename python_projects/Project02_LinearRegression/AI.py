"Linear Regression"

from sklearn.linear_model import LinearRegression

def regression():
	"""
	This is a linear regression program.
	It predicts a value using a simple dataset (input/output data, model details, and predictions).
	"""
	# Input and output data
	x = [[1], [2], [3], [4], [5], [6]]
	y = [1, 3, 5, 7, 9, 10]

	print("Input data (x):", x)
	print("Output data (y):", y)

	# Create and train model
	model = LinearRegression()
	model.fit(x, y)

	print("Model coefficients:", model.coef_)
	print("Model intercept:", model.intercept_)

	# Ask user for input
	try:
		user_value = float(input("Enter a value to predict: "))
		prediction = model.predict([[user_value]])
		print(f"Prediction for {user_value}: {prediction[0]}")
	except ValueError:
		print("Please enter a valid number.")

regression()

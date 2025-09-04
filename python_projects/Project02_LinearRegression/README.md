# Linear Regression Project
## Description
This project demonstrates a **simple linear regression** using python and scikit-learn.
The goal is to predict a numeric output `y` based on input `x` using a straight line that best fits the data.

Example data used in this project:
```example
x = [[1], [2], [3], [4], [5], [6]]
y = [1, 3, 5, 7, 9, 10]
```
The project uses **scikit-learn** to train a linear regression model and predict new values.
## Requirements
make sure you have **Python 3.x** installed. Then install the necessary libraries:
```requirements
pip install scikit-lean
```
 ### How to Run
 **1.** Open you terminal or command prompt.
 **2.** Navigate to the project folder:
 ```command
 cd path/to/your/project
 ```
 **3.** Run the Python script:
 ```Python
 python linear_regression.py
 ```
 **4.** The program will output the predicted values.

 Example:
 ```value
 print(model.predict([[4]]))
 ```

 ### Explanation
 **1. x:** Input data (features) as a 2D list.
 
 **2. y:** Output data (targets) as a 1D list.

 **3. LinearRegression():** Creates the linear regression model.

 **4. fit(x, y):** Trains the model on the given data.
 
 **5. predict([[user_value]]):** Predicts the output for user value.

### Example Input
```Input
Enter a value to predict: 5
```
### Example Output
```Output
Prediction for 4.0: 6.761904761904762
```
>Note: The predicted value may slightly differ due to imperfect linearity in the dataset.
# BMI-Calculator
BMI Calculator
This is a simple Python program that calculates the Body Mass Index (BMI) based on the user's weight and height.
It also interprets the BMI value into health categories such as Underweight, Normal weight, Overweight, and Obese.

 Features
•	Takes user input for weight (in kilograms) and height (in meters).
•	Calculates BMI using the standard formula:
BMI=weightheight2BMI = \frac{weight}{height^2}BMI=height2weight 
•	Categorizes the BMI result based on WHO standards.
•	Handles invalid or non-numeric inputs gracefully.

 How to Run
1.	Make sure Python 3.x is installed on your system.
2.	Save the Python code as bmi_calculator.py.
3.	Open a terminal or command prompt in the file's directory.
4.	Run the script using:
5.	python bmi_calculator.py
6.	Enter your weight in kilograms and height in meters when prompted.
Example Run
Enter your weight in kilograms: 60
Enter your height in meters: 1.65

Your BMI is: 22.04
Category: Normal weight

BMI Categories
BMI Range	Category
Below 18.5	Underweight
18.5 – 24.9	Normal weight
25.0 – 29.9	Overweight
30.0 and above	Obese

Error Handling
Ensures height and weight are positive numbers.
Displays an error message for invalid or non-numeric inputs.
 File Structure
bmi_calculator.py
README.md


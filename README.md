Project Summary: BMI Calculator Web Application
Objective
Create a web-based BMI (Body Mass Index) calculator that allows users to input their personal information, calculates their BMI, and provides feedback on their health status.

Features
User Input:

gender: Option to select Male or Female.
Age: Input for age.
Weight: Input for weight in kilograms.
Height: Input for height in meters.
Calculation:

Computes BMI using the formula:
BMI= weight (kg)/ height (m)2
 
Health Feedback:

Determines health status based on BMI value:
Underweight: BMI < 18.5
Normal weight: 18.5 ≤ BMI < 24.9
Overweight: 25 ≤ BMI < 29.9
Obesity: BMI ≥ 30

Technology Stack
Backend: Python with Flask
Handles form submissions.
Performs BMI calculations.
Stores user data in an SQLite database.
Frontend: HTML, CSS
HTML: Forms for user input and results display.
CSS: Styles to enhance the visual appearance of the web application.
Implementation Details
Backend:

Flask app (app.py):
Routes:
/: Displays the BMI calculator form.
/calculate: Processes form submissions and displays results.
SQLite Database (bmi_calculator.db):
Stores user inputs for future reference.
Frontend:

HTML Templates:
index.html: Form for user input.
result.html: Displays the BMI result and health status.
CSS (styles.css):
Styles the form, inputs, and overall layout to ensure a clean, user-friendly interface.
Project Structure
bash
/bmi calculator
    /static
        styles.css
        result.css
    /templates
        index.html
        result.html
    app.py
    bmi_calculator.db
Usage
Run the Application:

Execute python app.py to start the Flask server.
Access the application at http://127.0.0.1:5000/.
Interact with the Application:

Fill out the form with sex, age, weight, and height.
Submit the form to view the calculated BMI and health status.
Enhancements and Future Work
Add more advanced features such as:
User Authentication: To save and view historical BMI data.
Additional Metrics: Integrate with other health indicators.
Responsive Design: Ensure compatibility with mobile devices.

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def create_db():
    conn = sqlite3.connect("BMI_calculator.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gender TEXT,
                age INTEGER,
                weight REAL,
                height REAL,
                bmi REAL,
                health_status TEXT
            )
    ''')
    conn.commit()
    conn.close()


# def get_user_input():
#     gender = input("what gender are you? (male/female)").lower()
#     while gender not in ["male", "female"]:
#         gender = input("invalid input.Enter your gender(male/female): ").lower()
#     age = int(input("Enter your age: "))
#     weight = float(input("Enter your weight(in kgs'): "))
#     height = float(input("Enter your height(in meters i.e 1.75): "))
#     return gender, age, weight, height


def calculate_bmi(weight, height):
    bmi = round(weight / pow(height, 2), 2)
    return bmi


def determine_health_status(bmi):
    if bmi < 18.5:
        return "you are underweight"
    elif 18.5 <= bmi <= 24.5:
        return "healthy weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def store_user_info(gender, age, weight, height, bmi, health_status):
    conn = sqlite3.connect("BMI_calculator.db")
    cursor = conn.cursor()
    cursor.execute('''
            INSERT INTO user_info(gender, age, weight, height, bmi, health_status)
            VALUES(?, ?, ?, ?, ?, ?)
        ''', (gender, age, weight, height, bmi, health_status))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=["POST"])
def calculate():
    gender = request.form['gender']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    # was in main()
    bmi = calculate_bmi(weight, height)
    health_status = determine_health_status(bmi)

    # sql
    store_user_info(gender, age, weight, height, bmi, health_status)

    return render_template('result.html', bmi=bmi, health_status=health_status)


# def main():
#     gender, age, weight, height = get_user_input()
#     bmi = calculate_bmi(weight, height)
#     health_status = determine_health_status(bmi)
#     print(f"Your BMI status is {bmi} you're considered to be {health_status}")


if __name__ == "__main__":
    create_db()
    app.run(debug=True)

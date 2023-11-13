
from flask import Flask,render_template,request,url_for,session,redirect
from flask_mysqldb import MySQL
from datetime import *
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'mysql_user'
app.config['MYSQL_PASSWORD'] = 'Test@123'
app.config['MYSQL_DB'] = 'alnafi'
app.secret_key = 'somethingsomething'
mysql= MySQL(app)

@app.route('/')
def adm_page():
	return render_template('adm_form.html')

@app.route('/', methods=['POST','GET'])
def adm_form_create():
    if request.method == "POST":
        cur = mysql.connection.cursor()

        # Retrieve form data

        roll_no = (request.form['roll_no']).strip('\'')
        student_name = request.form['student_name']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        phone_number = request.form['phone_number']
        address = request.form['address']
        school_name = request.form['school_name']
        school_standard = request.form['school_standard']
        last_class_passed = request.form['last_class_passed']
        parent_name = request.form['parent_name']
        profession = request.form['profession']
        guardian1_name = request.form['guardian1_name']
        guardian1_tel = request.form['guardian1_tel']
        guardian2_name = request.form['guardian2_name']
        guardian2_tel = request.form['guardian2_tel']
        admission_fee = request.form['admission_fee']
        monthly_fee = request.form['monthly_fee']
        class_name = request.form['class_name']
        batch_time = request.form['batch_time']
        remark = request.form['remark']
        other_remark = request.form['other_remark']
        cdate = date.today()

        # Print values and their types
        print(f"roll_no: {roll_no}, type: {type(roll_no)}")
        print(f"student_name: {student_name}, type: {type(student_name)}")
        print(f"gender: {gender}, type: {type(gender)}")
        print(f"dob: {dob}, type: {type(dob)}")
        print(f"age: {age}, type: {type(age)}")
        print(f"phone_number: {phone_number}, type: {type(phone_number)}")
        print(f"address: {address}, type: {type(address)}")
        print(f"school_name: {school_name}, type: {type(school_name)}")
        print(f"school_standard: {school_standard}, type: {type(school_standard)}")
        print(f"last_class_passed: {last_class_passed}, type: {type(last_class_passed)}")
        print(f"parent_name: {parent_name}, type: {type(parent_name)}")
        print(f"profession: {profession}, type: {type(profession)}")
        print(f"guardian1_name: {guardian1_name}, type: {type(guardian1_name)}")
        print(f"guardian1_tel: {guardian1_tel}, type: {type(guardian1_tel)}")
        print(f"guardian2_name: {guardian2_name}, type: {type(guardian2_name)}")
        print(f"guardian2_tel: {guardian2_tel}, type: {type(guardian2_tel)}")
        print(f"admission_fee: {admission_fee}, type: {type(admission_fee)}")
        print(f"monthly_fee: {monthly_fee}, type: {type(monthly_fee)}")
        print(f"class_name: {class_name}, type: {type(class_name)}")
        print(f"batch_time: {batch_time}, type: {type(batch_time)}")
        print(f"remark: {remark}, type: {type(remark)}")
        print(f"other_remark: {other_remark}, type: {type(other_remark)}")
        print(f"cdate: {cdate}, type: {type(cdate)}")
        # Insert data into MySQL table

        cur.execute("""INSERT INTO adm_form (date, roll_no, student_name, gender, dob, age,
                        phone_number, address, school_name, school_standard, last_class_passed,
                        parent_name, profession, guardian1_name, guardian1_tel, guardian2_name,
                        guardian2_tel, admission_fee, monthly_fee, class_name, batch_time, remark,
                        other_remark) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""",
                    (cdate, roll_no, student_name, gender, dob, age, phone_number, address, school_name,
                     school_standard, last_class_passed, parent_name, profession, guardian1_name,
                     guardian1_tel, guardian2_name, guardian2_tel, admission_fee, monthly_fee,
                     class_name, batch_time, remark, other_remark))

        mysql.connection.commit()
        cur.close()

        return render_template('alert.html')
@app.route("/student_data",methods=['POST','GET'])		#http://127.0.0.1:5000/contact
def student_data():
		cursor = mysql.connection.cursor()
		sql = "select roll_no,date,student_name,gender,dob,age,phone_number,parent_name,batch_time from adm_form;"
		cursor.execute(sql)
		row =  cursor.fetchall()
		return render_template('trainer_report.html',output_data=row)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,jsonify,request
from flask_mysqldb import MYSQL
app=Flask(__name__)
app.congig['MYSQL_HOST']='localhost'
app.congig['MYSQL_USER']='root'
app.congig['MYSQL_PASSWORD']=''
app.congig['MYSQL_DB']='flask_crud'
mysql=MYSQL(app)
'''cur=mysql.connection.cursor()
cur.mysql.connection.cursor()
cur.execute("""create table if not exists students
(id int auto_increment primary key,
name varchar(100)not null,
email varchar(100)not null,
phone varchar(15)not null)""")
mysql.connection.commit()
cur.close()'''
@app.route('/students',methods=['GET'])
def get_students():
    try:
            cur=mysql.connection.cursor()
            cur.execute("select * from students")
            students=cur.fetchall()
            cur.close()
            data=[]
            for student in students:
                data.append({
                    "id":student[0],
                    "name":student[1],
                    "email":student[2],
                    "phone":student[3]
                })
            return jsonify({
                "success":True,
                "message":"students retreived successfully.",
                "count":len(data),
                "data":data
            }),200
    except Exception as e:
        return jsonify({
            "status":"error",
            "message":str(e)
        }),500
@app.route('/students',methods=['GET'])
def insert_students():
    try:
        data=request.get_json()
        if not data:
            return jsonify({
            "success":False,
            "message":"request body is required"
        }),400
        name=data.get("name")
        email=data.get("email")
        phone=data.get("phone")
        if not name or email or not phone:
            return jsonify({
                "success":False,
                "message":"name,email and phone are required"
            }),400
        cur=mysql.connection.cursor()
        cur.execute(
            "insert into satudents(name,email,phone)values(%s,%s,%s)"(name,email,phone))
        mysql.connection.commit()
        student_id=cur.lastrowid
        cur.execute("select * from student where id=%s",
                    (student_id,))
        student=cur.fetchone()
        cur.close()
        return jsonify({
            "success":True,
            "message":"student added successfully",
            "data":{
                "id":student[0],
                "name":student[1],
                "email":student[2],
                "phone":student[3],
            }
        }),201
    except Exception as e:
        mysql.connection.rollback()
        print(str(e))
        return jsonify({
            "success":False,
            "message":str(e)
        }),500
if __name__=='__main':
    app.run(debug=True)
        
        

                        

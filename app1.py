from flask import Flask,request,jsonify
import sqlite3
import os
app=Flask(__name__)
database=os.path.join(os.path.dirname(__file__),"students.db")
def get_db_connection():
    conn=sqlite3.connect(database)
    conn.row_factory=sqlite3.Row
    return conn
@app.route('/students',methods=['POST'])
def add_student():
    data=request.get_json()
    name=data['name']
    email=data['email']
    course=data['course']
    conn=get_db_connection()
    conn.execute(
        "insert into student(name,email,course)values(?,?,?)",(name,email,course))
    conn.commit()
    conn.close()
    return jsonify({
        "message":"student added successfully"
    }),201
@app.route('/students',methods=['GET'])
def get_students():
    conn=get_db_connection()
    students=conn.execute(
        "select * from students"
    ).fetchall()
    conn.close()
    result=[]
    for student in students:
        result.append({
            "id":student["id"],
            "name":student["name"],
            "email":student["email"],
            "course":student["course"]
        })
    return jsonify(result),200
@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
     data=request.get_json()
     name=data['name']
     email=data['email']
     course=data['course']
     conn=get_db_connection()
     conn.execute(
            """update students set=name=?,email=?,course=?,where id=?)""",
            (name,email,course,id)
            
        )
     conn.commit()
     conn.close()
     return jsonify({
                "message":"student updated successfully"
            }),200
@app.route('/students/<int:id>',methods=['Delete'])
def delete_student(id):
    conn=get_db_connection()
    conn.execute(
        "delete from students where id=?",(id,)
    )
    conn.commit()
    conn.close()
    return jsonify({
        "message":"student deleted successfully"
    }),200
    if __name__=='__main__':
        app.run(debug=True)
    

    


    
    
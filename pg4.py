from flask import Flask,jsonify,request
from flask_mysqldb import MYSQL
app=Flask(__name__)
app.congig['MYSQL_HOST']='localhost'
app.congig['MYSQL_USER']='root'
app.congig['MYSQL_PASSWORD']=''
app.congig['MYSQL_DB']='flask_crud'
mysql=MYSQL(app)
@app.route('/students/<int:id>',methods=['PUT'])
def update_student(id):
    try:
        data=request.get_json()
        if not sata:
            return jsonify({
                "success":False,
                "message":"request body is required."
            }),400
        name=data.get("name")
        email=data.get("email")
        phone=data.get("phone")
        if not name or not email or not phone:
            return jsonify({
                 "success":False,
                 "message":"name,email and phone are required."
                 }),400
        cur=mysql.connection.cursor()
        cur.execute("select * from students where id=%s",(id))
        student=cur.fetchone()
        if student is none:
            cur.close()
            return jsonify({
                "success":False,
                "message":"name,email and phone are required."
                }),404
        cur.execute("""
                    update students
                    set name=%s,email=%s,phone=%s,where id=%s
                    """,(name,email,phone,id))
        mysql.connection.commit()
        cur.execute("select * from students where id=%s",(id,))
        student=cur.fetchone()
        cur.close()
        return jsonify({
             "success":False,
                            "message":."

        })

        
        

        
                
            
    
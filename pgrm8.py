from flask import Flask,request,jsonify
import re
app=Flask(__name__)
def is_valid_email(email):
    pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern,email)
@app.route('/registration',methods=['POST'])
def register():
    data=request.get_json()
    name=data.get('name')
    email=data.get('email')
    if not name or not email:
        return jsonify({
            "status":"error",
            "message":"name and email are required."
            }),400
    if not is_valid_email(email):
        return jsonify({
            "status":"error",
            "message":"invalid email format."
        }),400
    return jsonify({
        "status":"success",
        "message":"student registered successfully.",
        "student":{
            "name":name,
            "email":email
        }
    }),201
if __name__=="__main__":
    app.run(debug=True)
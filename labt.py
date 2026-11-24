from flask import Flask,jsonify
app=Flask(__name__)
users=[
    {"id":1,
    "name":"uday",
    "email":"abcgmail.com",
    "age":20},
     {"id":2,
        "name":"mohan",
        "email":"123gmail.com",
        "age":19},
         {"id":3,
            "name":"vinay",
            "email":"ABCgmail.com",
            "age":20},
    ]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify({
        "success":True,
        "message":"users retrieved successfully.",
        "count":len(users),
        "data":users }),200
@app.route('/user/<int:id>',methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"]==id:
            return jsonify({
        "success":True,
        "message":"users retrieved successfully.",
        "data":user}),200
        return jsonify({"message":"user not found"}),404

if __name__=="__main__":
    app.run(debug=True)


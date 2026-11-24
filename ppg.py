from flask import Flask,jsonify
app=Flask(__name__)
users=[
    {
        "id":1,
        "name":"modi",
        "email":"modi@example.com",
        "age":25
    },
    {
      "id":2,
              "name":"nirmala",
              "email":"nirmala@example.com",
              "age":24  
    },
    {
        "id":3,
                "name":"seetha",
                "email":"seetha@example.com",
                "age":23
    },
    {
        "id":4,
                "name":"david",
                "email":"david@example.com",
                "age":22
    },
    {
        "id":5,
                "name":"geetha",
                "email":"geetha@example.com",
                "age":21
    }
]
@app.route('/users',methods=['GET'])
def get_users():
    return jsonify({
        "success":True,
        "message":"users retrieved successfully.",
        "count":len (users),
        "data":users
    }),200
@app.route('/users/<int:id>',methods=['GET'])
def get_user(id):
    for user in users:
        if user['id']==id:
            return jsonify({"success":True,
                    "message":"users retrieved successfully.",
                    "data":user
                }),200
    return jsonify({"message":"user not found"}),404
if __name__=="__main__":
    app.run(debug=True)



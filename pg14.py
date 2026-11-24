from flask import Flask,request,jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app=Flask(__name__)
orders=[]
@app.route("/")
def home():
    return"AI Shopping Cart API is running"
@app.route("/addOrders",methods=["POST"])
def add_oerders():
    data=request.get_json()
    orders.append(data)
    return jsonify({
        "success":True,
        "message":"Order added successfully",
        "data":data
    })
@app.route("/showOrders",methods=["GET"])
def show_orders():
    return jsonify({
            "success":True,
            "message":"Order added successfully",
            "data":orders
    })
@app.route("/ai-recommended",methods=["POST"])
def ai_recommend():
    data=request.get_json()
    username=data.get("user")
    user_orders=[
        order for order in orders
        if order.get("user")==username
    ]
    if not user_orders:
        return jsonify({
            "success":False,
            "message":"No orders found for this user"
        }),404
    prompt=f"""
You are a shopping assistant.jsonifyUser:{username}
Previous orders:
{user_orders}
suggest 2 or 3 useful products based on the
user's previous purchases.jsonify 
Give a short and simple explanation."""
    response=client.response.create(
        model="gpt-5-mini",
        input=prompt
    )
    recommendation=response.output_text
    return jsonify({
        "success":True,
        "user":username,
        "recommendation":recommendation
    })
if __name__=="__main__":
    app.run(debug=True)
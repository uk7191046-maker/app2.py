from flask import Flask,request,jsonify
import requests
app=Flask(__name__)
N8N_WEBHOOK_URL="https://udayappi.app.n8n.cloud/webhook-test/student-data"
@app.route("/student-data",methods=["post"])
def send_student():
    data=request.get_json()
    reponse=requests.post(
        N8N_WEBHOOK_URL,
        json=data
    )   
    print(reponse.json())
    return jsonify({
        "success":True,
        "message":"Data sent to N8N successfully",
        "n8n_response":reponse.text
        })

if __name__=="__main__":
    app.run(debug=True)
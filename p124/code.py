from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        'id': 1, 
        'name': u'Kanav', 
        'contact': u'4568703453', 
        'done': False
    },
    {
        'id': 2, 
        'name': u'Zeba', 
        'contact': u'5637458907', 
        'done': False
    }

]

@app.route("/add-data",methods=["POST"])
def createContact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    contact = {
        'id': contacts[-1]['id'] + 1, 
        'name': request.json['title'], 
        'contact': request.json.get('contact', ""), 
        'done': False
        }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    })
if (__name__=="__main__"):
    app.run()
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi"

# GET 
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Name",
        "email": "Name@gmail.com"
    }
    # get-user/Name?extra=new_name      (add data)
    extra = request.args.get("extra")  
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

 
# POST 
@app.route("/create-user", methods=["POST"])
def create_user():
    # if request.method == "POST":
    data = request.get_json()
    # do something 
    return jsonify(data), 201
        

if __name__ == "__main__":
    app.run(debug=True)

"""

Common HTTP methods
    GET 
    POST
    PUT
    DELETE

"""
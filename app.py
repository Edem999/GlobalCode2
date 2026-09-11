from flask import Flask,jsonify
app = Flask(__name__)

stu = [
    {
    "name" :"john doe",
    "id" :3,
    "age":30,
    "program":"ict"},
    {"name" :"joel tetteh",
    "id" :2,
    "age":120,
    "program":"ict"},
    {"name" :"jerry tetteh",
    "id" :1,
    "age":12,
    "program":"ict"},
    {"name" :"jeff tetteh",
    "id" :4,
    "age":23,
    "program":"ict"},
    {"name" :"ella tetteh",
    "id" :5,
    "age":34,
    "program":"ict"}
]

@app.route("/api/stu",methods =["GET"])
def get_data():
    return jsonify(stu)
if __name__ =="__main__":
    app.run(debug=True)

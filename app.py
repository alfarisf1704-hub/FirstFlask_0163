from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Class",methods=["POST"])
def firstflask():
    name = request.form.get("name")
    return f"hello,{name}, Kamu Keren banget udah bisa buat web ini!!!"

#http://127.0.0.1:5000
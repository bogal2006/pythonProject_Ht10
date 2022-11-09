from flask import Flask
app=Flask(__name__)
def calculate(a,b):
    c=a+b
    return c
@app.route("/")
def index():
    return f"This is payment. Pay{calculate(20,20)}"

if __name__=="__main__":
    app.run(host="127.0.0.1",port=8080,debug=True)
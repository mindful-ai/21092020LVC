from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")    # http://127.0.0.1:8080/  capturing the request
def index():       # This is the response
    return ( "<h1>Hello world!</h1>" )

@app.route("/today")    # 127.0.0.1:8080/today  capturing the request
def today():       # This is the response
    dt = datetime.now()
    format = "%A, %D %B, %Y %I:%M:%S %p"
    respstr = '<div style="background-color:Violet"><h1>' + dt.strftime(format) + '</h1></div>'
    return ( respstr )


if __name__ == "__main__":
    app.run()

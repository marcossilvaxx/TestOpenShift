from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/rennan")
def rennan():
    return "Rennan babaca"

def run(host='0.0.0.0', port=8080, debug=False):
    app.debug = debug
    app.run(host=host, port=port)

if __name__ == "__main__":
    run(debug='-d' in sys.argv or '--debug' in sys.argv)
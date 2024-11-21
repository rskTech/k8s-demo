from flask import Flask 
import os 
app = Flask(__name__) 
@app.route('/') 

def hello(): 
    return ('\nHello from Container World! \n\n')

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=8080, debug=True)

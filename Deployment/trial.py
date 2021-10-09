from flask import Flask

app = Flask('churn-app') # give an identity to your web service

@app.route('/ping',methods=['GET'])
def ping():
        return 'PONG'
    
if __name__=='__main__':
       app.run(debug=True, host="localhost", port=9696) # run the code in local machine with the debugging mode true and port 9696
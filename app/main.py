from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    print('app loaded!')
    return "<h1> hello, this is our first flask website<h1>";  
  
if __name__ =='__main__':  
    app.run(debug = True)  
from flask import Flask,make_response

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = make_response('<html></html>',302)
    headers = {
        'content-type':'text/plain',
        'location':'http://www.baidu.com'
    }
    response.headers = headers
    #return response
    return '<html></html>', 404, headers
    #return 'hello world!'

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0', debug=True)

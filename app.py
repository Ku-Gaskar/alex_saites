
from flask import Flask, render_template

app = Flask(__name__)








@app.route('/')
def index():
    content={}
    content['title'] = '100/100'

    return render_template('index.j2',content=content)

if __name__ == '__main__':
    app.run(host='192.168.1.102', port=8000, debug=True)
 
import qrcode as qr
from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('qr.html')

@app.route('/qrgenerator')
def qrgenerator():
    url= request.args.get('link')
    custom = request.args.get('qname')
    img= qr.make(url)
    img.save(f'static/images/{custom}.png')
    return render_template('img.html',custom=custom)

if __name__ == "__main__":
    app.run()
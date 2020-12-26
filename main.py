from flask import Flask, render_template, request, url_for, redirect
from helper import parse_doc, looper
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('intro.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)
        f.save('./tmp/' + secure_filename(f.filename))
    return redirect(url_for('parser', filename=f.filename))

@app.route('/parser')
def parser():
    filename = request.args['filename']
    parsed_data = parse_doc(filename)
    data = looper(parsed_data)
    for i in data:
        print(i)
    # os.remove('./tmp/{0}'.format(filename))
    return render_template('parser.html', data=data)

if __name__ == "__main__":
    # print("hello world\n")
    # # parse_pdf('')
    # parsed_data = parse_doc('')
    # looper(parsed_data)
    app.run(host='127.0.0.1', port=5000, debug=True)
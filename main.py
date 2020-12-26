from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('intro.html')


if __name__ == "__main__":
    # print("hello world\n")
    # # parse_pdf('')
    # parsed_data = parse_doc('')
    # looper(parsed_data)
    app.run(host='127.0.0.1', port=5000, debug=True)
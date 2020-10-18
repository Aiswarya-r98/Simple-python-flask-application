from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/oddeven', methods=['POST'])
def oddeven():
    number = int(request.form['number'])

    if(number % 2 == 0):
        msg = "The number is even"
    else:
        msg = "The number is odd"
    return render_template('index.html', message=msg)

if __name__=='__main__':
    app.run(debug=True)
    app.config['DEVELOPMENT'] = True
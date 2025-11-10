from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/Colombia')
def Colombia():
    return  render_template ('Colombia.html')

@app.route('/Brasil')
def Brasil():
    return render_template('Brasil.html')

@app.route('/Argentina')
def Argentina():
    return render_template('Argentina.html')



if __name__=='__main__':
    app.run(debug=True)


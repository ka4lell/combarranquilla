from flask import Flask, render_template

ft = Flask(__name__)

@ft.route('/')
def inicio():
    return render_template('futbol.html')

@ft.route('/condicionales')
def condicionales():
    return render_template('futbol.html', equipo="Colombia")

if __name__=='__main__':
    ft.run(debug=True)
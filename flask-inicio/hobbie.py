from flask import Flask, render_template

hobbie = Flask(__name__)

@hobbie.route('/')
def inicio():
    return render_template('inicio.html')

@hobbie.route('/Videojuegos')
def Colombia():
    return  render_template ('Videojuegos.html')

@hobbie.route('/Musica')
def Brasil():
    return render_template('Musica.html')

@hobbie.route('/Peliculas')
def Argentina():
    return render_template('Peliculas.html')



if __name__=='__main__':
    hobbie.run(debug=True)


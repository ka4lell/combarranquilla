from flask import Flask, render_template, request

sum = Flask(__name__)

@sum.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        numero1 = int(request.form["Numero1"])
        numero2 = int(request.form["Numero2"])
        total = numero1 + numero2
        return render_template('res.html', total=total, numero1=numero1, numero2=numero2)
    return render_template('formm.html')


if __name__ =='__main__':
    sum.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "Hola mi nueva pagina Python"
    return render_template('index.html')

@app.route('/about')
def about():
    # return "Acerca de Agejove.co"
     return render_template('about.html')

@app.route('/contact')
def contact():
    # return "Acerca de Agejove.co"
     return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
    # cuando este en modo de prueba colocar True



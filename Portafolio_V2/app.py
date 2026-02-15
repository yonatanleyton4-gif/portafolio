from flask import Flask, render_template

app = Flask(__name__)

# Ruta para el Inicio
@app.route('/')
def home():
    # Buscamos el index dentro de la carpeta INICIO
    return render_template('INICIO/index.html')

# Ruta para Proyectos
@app.route('/proyectos')
def proyectos():
    return render_template('PROYECTOS/index.html')

# Ruta para Sobre Mí
@app.route('/sobre-mi')
def sobre_mi():
    return render_template('SOBRE MI/index.html')

# Ruta para Contacto
@app.route('/contacto')
def contacto():
    return render_template('CONTACTO/index.html')

if __name__ == '__main__':
    app.run(debug=True)
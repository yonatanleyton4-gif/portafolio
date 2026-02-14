from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    proyectos_web =[
        {"nombre": "Portafolio V2", "tech": "flask & Python","status":"En proceso"},
        {"nombre": "Tienda Mooca", "tech": "JS & Python","status":"Pendiente"},
        {"nombre": "App Clima", "tech": "APIs","status":"pendiente"}
    ]
    return render_template("index.html", proyectos=proyectos_web)

if __name__ == "__main__":
    app.run(debug=True)
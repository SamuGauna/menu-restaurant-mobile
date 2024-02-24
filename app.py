from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/pasta')
def pasta():
    ruta_actual= os.path.basename(request.path)
    print(ruta_actual)
    menuPasta = [
        {"name": "Spaghetti", "price": 5000, "description": "Spaghettis caseros con salsa bolognesa"},
        {"name": "Ravioles", "price": 7000, "description": "Ravioles caseros con salsa bolognesa"},
        {"name": "Ñoquis", "price": 8000, "description": "Ñoquis caseros con salsa bolognesa"}
    ]
    return render_template('menuOptions.html', menu=menuPasta, ruta_actual=ruta_actual)
@app.route('/pizza')
def pizza():
    ruta_actual= os.path.basename(request.path)
    menuPizza = [
        {"name": "Cuatro Quesos", "price": 5000, "description": "Masa a la piedra"},
        {"name": "Fuggazetta", "price": 7000, "description": "Masa a la piedra, porcion familiar"},
        {"name": "Muzzarella", "price": 8000, "description": "Masa a la piedra, porcion familiar"}
    ]
    return render_template('menuOptions.html', menu=menuPizza, ruta_actual=ruta_actual)

if __name__ == '__main__':
    app.run(debug=True)
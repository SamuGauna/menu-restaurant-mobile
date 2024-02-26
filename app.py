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
@app.route('/burguer')
def burguer():
    ruta_actual= os.path.basename(request.path)
    menuBurguer = [
        {"name": "Americana", "price": 5000, "description": "USA Burguer"},
        {"name": "Doble cheese", "price": 7000, "description": "Doble queso cheedar"},
        {"name": "Bacon", "price": 8000, "description": "Rebasada de Bacon"}
    ]
    return render_template('menuOptions.html', menu=menuBurguer, ruta_actual=ruta_actual)
@app.route('/papas')
def papas():
    ruta_actual= os.path.basename(request.path)
    menupapas = [
        {"name": "Cheedar", "price": 5000, "description": "Para los amantes del cheedar"},
        {"name": "Doble chrunch", "price": 7000, "description": "Super crujientes"},
        {"name": "Bacon", "price": 8000, "description": "Acompañas del mejor bacon"}
    ]
    return render_template('menuOptions.html', menu=menupapas, ruta_actual=ruta_actual)
@app.route('/picada')
def picada():
    ruta_actual= os.path.basename(request.path)
    menupicada = [
        {"name": "Picada de pollo", "price": 5000, "description": "Pollo, Papa a la francesa, Ensalada, Queso costeño y Salsa de la casa"},
        {"name": "Picada de carne", "price": 7000, "description": "Carne, Papa a la francesa, Ensalada, Queso costeño y Salsa de la casa"},
        {"name": "Picada Mixta", "price": 8000, "description": "Cerdo, Pollo, Papa a la francesa, Ensadala, Queso costeño, y Salsa de la casa"}
    ]
    return render_template('menuOptions.html', menu=menupicada, ruta_actual=ruta_actual)
@app.route('/bebida')
def bebida():
    ruta_actual= os.path.basename(request.path)
    menubebida = [
        {"name": "Cosmopolitan", "price": 5000, "description": "Lorem ipsum"},
        {"name": "Margarita", "price": 7000, "description": "Lorem ipsum"},
        {"name": "Fernet", "price": 8000, "description": "Lorem ipsum"}
    ]
    return render_template('menuOptions.html', menu=menubebida, ruta_actual=ruta_actual)
if __name__ == '__main__':
    app.run(debug=True)
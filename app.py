import requests

from flask import (
    Flask, 
    render_template, 
    request,
    redirect,
)

#creo el objeto flask
app = Flask(__name__)

#aca van lo declarado previamente
lista_obj = [
    dict(
        categoria = 'Electrodomesticos',
        nombre = 'Lavavajillas',
        precio = '130.000',
        descripcion = 'Instrumento util para el lavado de la vajilla familiar.',
        stock = '23'
    ),
    dict(
        categoria = 'Computacion',
        nombre = 'Memoria RAM',
        precio = '180.000',
        descripcion = 'Elemento util para el armado de una computadora',
        stock = '28'
    ),
    dict(
        categoria = 'Tecnologia',
        nombre = 'Televisor',
        precio = '200.000',
        descripcion = 'Televisor de 60 pulgadas, marca LG',
        stock = '4'
    )
]

#esta lista era para probar la API, no la uso
#lista_requerida = requests.get('https://fakerapi.it/api/v1/custom?_quantity=3&_locale=es_AR&categoria=city&nombre=pokemon&precio=buildingNumber&descripcion=card_number&stock=buildingNumber')

#aca las routes
@app.route('/')
def index():
    return render_template(
        'index.html',
    )
    
@app.route('/productos')
def productos():
    lista = lista_obj
    return render_template(
        'productos.html',
        lista = lista,
    )
    
@app.route('/agregar_productos', methods= ['GET','POST'])
def agregar_productos():
    
    if request.method == 'POST':
        cat = request.form['categoria']
        name = request.form['nombre']
        price = request.form['precio']
        desc= request.form['descripcion']
        stock = request.form['stock']
    
        #creo el objeto para añadirlo al diccionario que uso para la tabla
        prod = dict(
            categoria = cat,
            nombre = name,
            precio = price,
            descripcion = desc,
            stock = stock,
        )
        #asigno prod al diccionario
        lista_obj.append(prod)
        #redirecciono
        return redirect('productos')
    
    return render_template(
        'agregar_productos.html',
    )

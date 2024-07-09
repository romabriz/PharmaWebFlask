'''pip install flask'''
'''flask run / para ejecutar todo el codigo'''
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'farmacia_productos'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/CRUD')
def CRUD():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM productos')
    data = cur.fetchall()
    return render_template('CRUD.html', productos = data)

# AGREGAR, CREATE
@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO productos (nombre, marca, cantidad, precio) VALUES (%s, %s, %s, %s)',(nombre, marca, cantidad, precio))
        mysql.connection.commit()
        flash('Producto agregado correctamente')
    return redirect(url_for('CRUD'))

# EDITAR, MODIFICAR
@app.route('/editar/<id>')
def obtener_producto(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM productos WHERE id = {id}")  #SELECT * FROM contacts WHERE id = %s', (id) 
    data = cur.fetchall() #Obtiene un unico dato
    return render_template('editar_producto.html', producto = data[0])

@app.route('/actualizar/<id>', methods = ['POST'])
def actualizar_producto(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE productos 
                SET nombre = %s,
                    marca = %s,
                    cantidad = %s,
                    precio = %s
                WHERE id = %s
                """, (nombre, marca, cantidad, precio, id))
        mysql.connection.commit()
        flash('Producto modificado correctamente')
        return redirect(url_for('CRUD'))

# ELIMINAR, DELETE
@app.route('/borrar/<string:id>')
def borrar_producto(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM productos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Producto eliminado correctamente')
    return redirect(url_for('CRUD'))


if __name__ == '__main__':
    app.run(debug=True)



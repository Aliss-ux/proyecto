#librerias para las distintas extensiones de flask
from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Ali'
app.config['MYSQL_PASSWORD'] = 'Alina99'
app.config['MYSQL_DB'] = 'buzon'
mysql = MySQL(app) 

#settings
app.secret_key= 'mysecretkey'

#ruta de peticion a la pagina principal
@app.route('/')
def Index():
    return render_template('index2.html')

# metodo para datos a la tabla de base de datos
@app.route('/datos', methods=['POST'])
def datos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        celular = request.form['celular'] 
        motivo = request.form['motivo']
        mensaje = request.form['mensaje']
        #cursor 
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO almacen (Nombre, Correo, Celular, Motivo, Mensaje) VALUE (%s, %s, %s, %s, %s)', (nombre, correo, celular, motivo, mensaje)) 
        mysql.connection.commit()
        return redirect(url_for('Index'))  #ejecuta la operacion principal 

#metodo para guardar los usuarios
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        user = request.form['usuario']
        contraseña = request.form['contraseña']
        cur = mysql.connection.cursor()
       # cur.execute('INSERT INTO usuario (Usuario, Contraseña) VALUE (%s, %s)', (user, contraseña)) 
        #mysql.connection.commit()
        #print (user)
        #return redirect( url_for('tabla') )

        cur.execute('select count(usuario) from Admin WHERE Usuario= (%s)'%(user))
        #cur.execute('SELECT * FROM usuario WHERE Usuario = {0}'.format(user))
        data = cur.fetchone()[0]
        mysql.connection.commit()
        if data > 0:
            cur.execute('SELECT * FROM Admin WHERE Usuario=(%s)'%(user))
            dato = cur.fetchall()[0];
            dato= dato[1]
            mysql.connection.commit()
            if dato == contraseña:
                return redirect(url_for('tabla'))
            else:
                flash('Contraseña Incorrecta')
                return redirect(url_for('login2'))
        else :
           flash('El usuario no existe')
           return redirect(url_for('login2'))




#manda datos a la tabla de base de datos
@app.route('/tabla')
def tabla():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM almacen')
    data = cur.fetchall()   #sacar datos en el cursor
    cur.close()
    return render_template('admin.html', contacts = data)

#borra datos de la base de datos
@app.route('/borrar/<string:id>')
def borrar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM almacen WHERE id = {0}'.format(id))
    mysql.connection.commit()
    return redirect( url_for('tabla') )

@app.route('/login2')
def login2():
    return render_template('ingresa.html')

#hace funcionar 
if __name__== '__main__':
    app.run(port=5000, debug= True)
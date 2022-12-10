from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from termcolor import colored


app  =Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'   #Especificamos servidor usuario contraseña y DB
app.config['MYSQL_USER']= 'lucho'   
app.config['MYSQL_PASSWORD']= '24041992'   
app.config['MYSQL_DB']= 'flaskcontacts'   
mysql = MySQL(app) 
# settings
app.secret_key = 'mysecretkey'     #Le decimos como va a ir protegida la seccion

@app.route('/')        #cada vez que el usuario entre aca vamos a responderle algo
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM flaskcontacts')      #Declaracion de la consulta
    data = cur.fetchall()      #Obtenemos los datos de la consutla de arriba 
    print(colored(data,'red'))

    return render_template('index.html', contacts = data)   


@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']       #Tomo el dato que viene del from index.html
        phone = request.form['phone']       #Tomo el dato que viene del from index.html
        contact = request.form['contact']       #Tomo el dato que viene del from index.html
               
        print(fullname,phone,contact)
        cur = mysql.connection.cursor()     #Cursos que me permite ejecutar las sql --  obtenemos la conexion
        cur.execute('INSERT INTO flaskcontacts (fullname,phone,contact)  VALUES (%s,%s,%s)', (fullname,phone,contact))
        mysql.connection.commit()      #Ejecutamos la consulta
        flash('Contact added succesfully!')
        return redirect(url_for('Index'))       #Redireccionamos al inicio una vez ingresados los datos


@app.route('/edit')        #cada vez que el usuario entre aca vamos a responderle algo
def edit_contact():
    return

@app.route('/delete/<string:id>')        #cada vez que recibas una ruta delete debe tener al lado un nro que es el id para eliminarlo
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM flaskcontacts WHERE id = {0}'.format(id))
    mysql.connection.commit()      #Ejecutamos la consulta

    flash('Contact removed succesfully!')
    return redirect(url_for('Index'))
        


if __name__ == '__main__':      #Si el archivo que arranca todo es app.py comienza el servidor 
    app.run(port = 3000, debug= True) #Especificamos el puerto. Debug = True hace que reinicie automaticamente cada vez que hacemos cambios en el servidor 

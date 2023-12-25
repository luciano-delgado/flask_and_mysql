from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from termcolor import colored

# Este es un cambio para ver como figura en git 
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
    cur.execute('SELECT * FROM oyp_tasks_management')      #Declaracion de la consulta
    data = cur.fetchall()      #Obtenemos los datos de la consutla de arriba 
    print(colored(data,'red'))

    return render_template('index.html', datos = data)   


@app.route('/add_task', methods = ['POST'])
def add_task():
    if request.method == 'POST':
        sector = request.form['sector']       #Tomo el dato que viene del from index.html
        solicitante = request.form['solicitante']       #Tomo el dato que viene del from index.html
        requerimiento = request.form['requerimiento']       #Tomo el dato que viene del from index.html
               
        print(sector,solicitante,requerimiento)
        cur = mysql.connection.cursor()     #Cursos que me permite ejecutar las sql --  obtenemos la conexion
        cur.execute('INSERT INTO oyp_tasks_management (sector,solicitante,requerimiento)  VALUES (%s,%s,%s)', (sector,solicitante,requerimiento))
        mysql.connection.commit()      #Ejecutamos la consulta
        flash('task added succesfully!')
        return redirect(url_for('Index'))       #Redireccionamos al inicio una vez ingresados los datos


@app.route('/edit/<id>')        #cada vez que el usuario entre aca vamos a responderle algo
def get_task(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM  oyp_tasks_management WHERE ID = %s', (id))
    data = cur.fetchall()
    print(colored(data[0],'blue'))

    return render_template('edit_requerimiento.html', descripcion = data[0])

@app.route('/update/<id>', methods = ['POST'])        #cada vez que el usuario entre aca vamos a responderle algo
def update_task(id):
    if request.method == 'POST':
        sector = request.form['sector']
        solicitante = request.form['solicitante']
        requerimiento = request.form['requerimiento']

        cur = mysql.connection.cursor()

        # %s porque le voy a pasar string
        cur.execute(
            """
        UPDATE oyp_tasks_management
        SET sector = %s,
            solicitante = %s,
            requerimiento = %s
        WHERE ID = %s
        """,
         (sector,solicitante, requerimiento, id )
         )

        mysql.connection.commit()
        flash('task updated succesfully!')

        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')        #cada vez que recibas una ruta delete debe tener al lado un nro que es el id para eliminarlo
def delete_task(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM oyp_tasks_management WHERE id = {0}'.format(id))
    mysql.connection.commit()      #Ejecutamos la consulta

    flash('task removed succesfully!')
    return redirect(url_for('Index'))
        


if __name__ == '__main__':      #Si el archivo que arranca todo es app.py comienza el servidor 
    app.run(port = 3000, debug= True) #Especificamos el puerto. Debug = True hace que reinicie automaticamente cada vez que hacemos cambios en el servidor 

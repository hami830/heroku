from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL
app = Flask(__name__)
app.secret_key = "flash message"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='mamadou'
app.config['MYSQL_PASSWORD']='mamadou96'
app.config['MYSQL_DB']='CrudApplication'
mysql = MySQL(app)
@app.route('/')
def Index():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM Apprenants")
	data =cur.fetchall()
	cur.close()
	return render_template('index.html', Apprenants = data)
@app.route('/insert', methods = ['POST'])
def insert():
	if request.method == "POST":
		flash("Data Inserted Successfully")  
		Nom = request.form['Nom']
		Prenom = request.form['Prenom']
		Age = request.form['Age']
		Email = request.form['Email']
		Telephone = request.form['Telephone']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Apprenants(Nom, Prenom, Age, Email, Telephone) VALUES(%s, %s, %s, %s, %s)",(Nom, Prenom, Age, Email, Telephone))
		mysql.connection.commit()
		return redirect(url_for('Index'))
@app.route('/update', methods = ['POST', 'GET'])
def update():
	if request.method == 'POST':
		id_data = request.form['id']
		Nom = request.form['Nom']
		Prenom = request.form['Prenom']
		Age = request.form['Age']
		Email = request.form['Email']
		Telephone = request.form['Telephone']
		cur = mysql.connection.cursor()
		cur.execute("""
		UPDATE Apprenants
		SET Nom=%s, Prenom=%s, Age=%s, Email=%s, Telephone=%s
		WHERE id=%s



		""", (Nom, Prenom, Age, Email, Telephone, id_data))
		flash("Data Update Successfully")
		mysql.connection.commit()
		return redirect(url_for('Index'))
@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):
	flash("Data Deleted Successfully")
	cur = mysql.connection.cursor()
	cur.execute("DELETE FROM Apprenants WHERE id = %s", (id_data))
	mysql.connection.commit()
	return redirect(url_for('Index')) 


if __name__ == '__main__':
	app.run(debug=True)
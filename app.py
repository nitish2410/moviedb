import mysql.connector
from flask import Flask,render_template,request

try:
	conn=mysql.connector.connect(host="database-1.crw3zlspcgvl.us-east-2.rds.amazonaws.com",user="admin",password="admin1234",database="movies")

	mycursor=conn.cursor()
except Exception as e:
	print("Some error occured")

mycursor.execute("SELECT * FROM movie")
data=mycursor.fetchall()

application = app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',data=data[0])

if __name__=="__main__":
	app.run(debug=True)
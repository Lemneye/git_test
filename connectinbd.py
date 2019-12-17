#coding:utf-8 
import sqlite3
connection=sqlite3.connect("gestionL.db")
cursor=connection.cursor()
print(type(connection))
print(type(cursor))
user_namee=("lemneye",)
#cursor.execute('SELECT * FROM tusers WHERE user_name="lemneye"')
cursor.execute('SELECT * FROM tusers WHERE user_name=?',user_namee)
resultat=cursor.fetchone()[1]
print(resultat)

connection.close()
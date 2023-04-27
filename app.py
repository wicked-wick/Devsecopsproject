import sqlite3
from flask import Flask, render_template, request, jsonify
app=Flask(__name__,static_folder='static')
Secret='ae23132e21dada12414'
Password='Pythonispower'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search')
def search():
    search_term=request.args.get('q')
    conn=sqlite3.connect('football.db')
    cur=conn.cursor()
    cur.execute("Select * from playerstb where name LIKE ?",('%'+search_term+'%',))
    records=cur.fetchall()
    conn.close()
    return render_template('results.html',records=records,search_term=search_term)

if __name__=='__main__':
    app.run(debug=True)

import sqlite3
from flask import Flask, render_template, request, jsonify, abort, render_template_string
app=Flask(__name__,static_folder='static')
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
@app.route('/files')
def files():
    term=request.args.get('get')
    if not term:
        abort(400,'Parameter get not found in the url')
    template=f'''<div><h1>Hello</h1>{term}</div>'''
    return render_template_string(template)
if __name__=='__main__':
    app.run(debug=True)

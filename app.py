from operator import itemgetter
from flask import Flask,render_template,request
import sqlite3

app=Flask('__name__')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        regno = request.form.get('regno')
        phone = request.form.get('phone')
        year = request.form.get('year')
        dept = request.form.get('dept')
        date = request.form.get('date')
        time = request.form.get('time')
        purpose = request.form.get('purpose')
        print(date)
        print(time)

        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO PASS VALUES(?,?,?,?,?,?)",(name,regno,phone,year,dept,purpose))
        cur.execute("select * from PASS")
        t = cur.fetchall()
        for i in t:
            print(i)
        conn.commit()
        conn.close()
        return "DATA ENTERED"
    return render_template('Gate Pass Generator.html')

@app.route('/index')
def index():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("select * from PASS")
    t = cur.fetchall()
    conn.commit()
    conn.close()
    nos = len(t)
    names = list(map(itemgetter(0),t))
    regnos = list(map(itemgetter(1),t))
    phones = list(map(itemgetter(2),t))
    years = list(map(itemgetter(3),t))
    depts = list(map(itemgetter(4),t))
    purposes = list(map(itemgetter(5),t))
    print(nos)
    return render_template('Gate Pass Index.html',n = nos,a = names,b = regnos,c = phones,d = depts,e = years,f = purposes)


if __name__ == "__main__":
    app.run(debug=True)


    
    

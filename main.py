from flask import Flask, render_template
import util

app = Flask(__name__)

username='williamsa'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# 127.0.01:5000/api/update_basket_a
@app.route('/api/update_basket_a')
def index():
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    check = util.run_and_commit_sql(cursor,connection,"INSERT INTO basket_a VALUES (5,'Cherry')")

    util.disconnect_from_db(connection,cursor)
    
    if check == 1:
        return render_template('index.html', log_html = "Success")  
    else:
        return render_template('index.html' , log_html = check)

# 127.0.0.1:5000/api/unique
@app.route('/api/unique')
def index2():
    cursor, connection = util.connect_to_db(username,password,host,port,database)

    recordA, check = util.run_and_fetch_sql(cursor, "SELECT a,fruit_a FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b WHERE b IS NULL;")

    if check == -1:
        return render_template('index.html',log_html=recordA)
    else:
        col_namesA = [desc[0] for desc in cursor.description]
        logA = recordA
    
    recordB, check = util.run_and_fetch_sql(cursor, "SELECT b,fruit_b FROM basket_a FULL OUTER JOIN basket_b ON fruit_a = fruit_b WHERE a IS NULL;")
    
    if check == -1:
        return render_template('index.html',log_html=recordB)
    else:
        col_namesB = [desc[0] for desc in cursor.description]
        logB = recordB

    util.disconnect_from_db(connection,cursor)
    return render_template('index2.html', sql_tableA = logA, table_titleA=col_namesA, sql_tableB =logB, table_titleB = col_namesB)



if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

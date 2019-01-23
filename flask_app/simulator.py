#!/usr/bin/env python
import optparse
import MySQLdb
import random
import sys
import json
#sys.path.append('/ws/dhavnoor-bgl/flask_pkg/lib/python2.7/site-packages')
sys.path.append('/ws/dhavnoor-bgl/python_packages/lib/python2.7/site-packages')
from flask import Flask,request

app = Flask(__name__)

def get_mysql_conn():

    conn = MySQLdb.connect (host = 'localhost',
                            user = 'root1',
                            passwd = 'Admin12@',
                            db = 'dars')
    return conn

@app.route("/total_msg")
def total_msg():
    conn = get_mysql_conn()
    cursor = conn.cursor ()
    cursor.execute("""
		   select count(*) from messages;
                   """)
    data = cursor.fetchone()
    print data[0]
    cursor.close()
    conn.commit()
    conn.close()
    if data is None:
        return "No data preseng"
    else:
        return '{"total_msg" :' +str(data[0])+'}'
       
@app.route("/total_err_msg")
def total_err_msg():
    conn = get_mysql_conn()
    cursor = conn.cursor ()
    cursor.execute("""
		   select count(*) from messages where message_type = "'ERROR'";
                   """)
    data = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    print data[0]
    if data is None:
        return "No data present"
    else:
        return '{"total_err_msg" :' +str(data[0])+'}'

@app.route("/total_info_msg")
def total_info_msg():
    conn = get_mysql_conn()
    cursor = conn.cursor ()
    cursor.execute("""
		   select count(*) from messages where message_type = "'INFO'";
                   """)
    data = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    print data[0]
    if data is None:
        return "No data present"
    else:
        return '{"total_info_msg" :' +str(data[0])+'}'

@app.route("/total_warning_msg")
def total_warning_msg():
    conn = get_mysql_conn()
    cursor = conn.cursor ()
    cursor.execute("""
		   select count(*) from messages where message_type = "'WARNING'";
                   """)
    data = cursor.fetchone()
    cursor.close()
    conn.commit()
    conn.close()
    print data[0]
    if data is None:
        return "No data present"
    else:
        return '{"total_warning_msg" :' +str(data[0])+'}'

def main():   
    parser = optparse.OptionParser()   
    parser.add_option("--host","-H", dest="host", help="hostname or IP for Mysql");
    parser.add_option("--user","-u", dest="user", help="username for Mysql");
    parser.add_option("--password","-p", dest="pswd", help="password for Mysql");
    parser.add_option("--db","-d", dest="db_name", help="dbname for Mysql");
    parser.add_option("--num_records","-n", dest="num_rec", help="number of records to add");
    
    (options, args) = parser.parse_args()   
  
        
    total_msg()
    total_err_msg()
    total_info_msg()
    total_warning_msg()
    #total_alert_msg()
    #cursor.close()
    #conn.commit()
    #conn.close()

if __name__ == '__main__':
    app.run(host='bgl-ads-523',debug=True)
    main()

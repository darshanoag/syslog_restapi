#!/usr/bin/env python
import optparse
import MySQLdb
import random

def main():   
    parser = optparse.OptionParser()   
    parser.add_option("--host","-H", dest="host", help="hostname or IP for Mysql");
    parser.add_option("--user","-u", dest="user", help="username for Mysql");
    parser.add_option("--password","-p", dest="pswd", help="password for Mysql");
    parser.add_option("--db","-d", dest="db_name", help="dbname for Mysql");
    parser.add_option("--num_records","-n", dest="num_rec", help="number of records to add");
    
    (options, args) = parser.parse_args()   
    error_type = ["ERROR","WARNING","NOTIFICATION","ALERT","INFO","DEBUG"]
  
        
    conn = MySQLdb.connect (host = options.host,
                            user = options.user,
                            passwd = options.pswd,
                            db = options.db_name)
    cursor = conn.cursor ()
    cursor.execute ("""CREATE TABLE IF NOT EXISTS messages(id int(11) NOT NULL AUTO_INCREMENT,timestamp varchar(25),ip_address varchar(25),message_type varchar(20),description varchar(255),PRIMARY KEY (id))""")
    for i in range(1,int(options.num_rec)):
        ip = str(random.randint(1,101))+'.'+str(random.randint(1,101))+'.'+str(random.randint(1,101))+'.'+str(random.randint(1,101))
        err_index = random.randint(1,101) % 6
        description = "This is message number: "+str(random.randint(1,101))
        cursor.execute ("""
                        INSERT INTO messages(timestamp,ip_address,message_type,description)
                        VALUES ("09-12-2018","%s","%s","%s")
                        """,(ip,error_type[err_index],description))
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

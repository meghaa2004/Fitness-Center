import mysql.connector as sql

fit=sql.connect(host='localhost',user='root',passwd='qwerty',database='fit_project', auth_plugin='mysql_native_password')
if fit.is_connected():
    print('connected')
    c1=fit.cursor()
    c1.execute('create table customer(custmer varchar(100) primary key,custmer_name varchar(100),custmer_address varchar(1000),joined_date varchar(100),amt_paid varchar(100))')    
    fit.commit()
    print('table created')
        

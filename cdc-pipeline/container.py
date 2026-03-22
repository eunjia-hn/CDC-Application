import os
import sys
import pymysql

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql and cassandra, mongodb and redis do not need it

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# delete container
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
        password='rootuser',
        host='127.0.0.1')

    # create cursor
    cursor = cnx.cursor()

    # delete previous db
    query = ("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute(query)

    # create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    # use db
    query = ("USE pluto")
    cursor.execute(query)

    # create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cursor.execute(query)

    # clean up
    cnx.commit()
    cursor.close()
    cnx.close()    

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]     
# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 5600:5600 --name final_mysql_container -e MYSQL_ROOT_PASSWORD=rootuser -d mysql', 'mysql')
    create('docker run -p 27017:27017 --name final_mongo_container -d mongo', 'mongo') # port issue experienced changed to 27017 
    create('docker run -p 2400:2400 --name final_redis_container -d redis', 'redis')
    create('docker run -p 1000:1000 --name final_cassandra_container -d cassandra', 'cassandra')
    sys.exit()
# if -delete input argument, delete containers
if(argument == '-delete'):
    delete('final_mysql_container')
    delete('final_mongo_container')
    delete('final_redis_container')
    delete('final_cassandra_container')
    sys.exit()
# if -init, init mysql and cassandra, mongodb does not need it
if(argument == '-init'):
    init_mysql()
    sys.exit()
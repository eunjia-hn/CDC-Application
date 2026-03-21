import os
import sys

# ----------------
# input arguments
# ----------------
# -create, create containers

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

# read input argument
argument = len(sys.argv)
if (argument > 1):    
    argument = sys.argv[1]   

# if -create input argument, create containers
if(argument == '-create'):
    print("Creating containers...")
    create('docker run -p 3307:3307 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyPassword -d mysql', 'mysql')
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongo')
    create("docker run -p 6379:6379 --name some-redis -d redis", "redis")
    create("docker run -p 9042:9042 --name some-cassandra -d cassandra", "cassandra")


# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if (result == 0):
        cmd = f'docker rm {container}'
        result = os.system(cmd)
        print(f'Removed {container}')

# if -delete input argument, delete containers
if(argument == '-delete'):
    print("Deleting containers...")
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')
    delete('some-cassandra')

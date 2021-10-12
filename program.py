import pandas as pd
import numpy as np
import mysql.connector as mysql

                                 # Function to create database
def create_database(cursor):
    sql="CREATE DATABASE IF NOT EXISTS trexno;"
    cursor.execute(sql)
                                   # Function to create Table
def create_table(cursor):
    database="use trexno;"
    cursor.execute(database)
    sql="create table IF NOT EXISTS student (S_No int not null PRIMARY KEY,Name varchar(100),Regs_No bigint);"
    cursor.execute(sql)
                                  # Function to insert data from csv into MYSQL Database
def insert_record(cursor):
    record=pd.read_csv("list1.csv")
    record=np.array(record)
    print("Inserting data...")
    print(record)
    for row in record:
        cursor.execute('INSERT INTO student' 'VALUES(%s, %s, %s)', row)
    print("Record Inserted.")

             # Database Credential Part. Change credential of this part according to your MySQL Database credential.
conn=mysql.connect(host='localhost',user='root', password='')

if conn.is_connected():
    print("Connected to Mysql")
    cursor = conn.cursor()
                             # Calling all above created functions if database is connected.
    create_database(cursor)
    create_table(cursor)
    insert_record(cursor)


# internal
import connectin

# standard
import sqlite3
import os


#################### INSERT DATA TO DATABASE ####################

def insert_post(title,description,category_id):
    '''This function insert title, descripton and category_id to post table from blog database'''
    insert_data = """
        INSERT INTO post(title, description, category_id)
        VALUES(?, ?, ?)
    """
    info = (title, description, category_id)
    conn = connectin.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    conn.commit()
    conn.close()
    

def insert_category(name):
    '''This function insert name of category to category table'''
    insert_data = """
        INSERT INTO category(name)
        VALUES(?)
    """
    info = (name,)
    conn = connectin.db_connection()
    cursor = conn.cursor()
    cursor.execute(insert_data, info)
    cursor.close()
    conn.commit()
    conn.close()

#################### READ DATA FROM DATABASE ####################

def id_and_title():
    '''This function return id and title column from post table'''
    conn = connectin.db_connection()
    cursor = conn.cursor()
    show_post_table = """
            SELECT id, title
            FROM post
        """
    data = ['id : title']
    for row in cursor.execute(show_post_table):
        data.append(f'{row[0]} : {row[1]}')

def read_all_category():
    pass
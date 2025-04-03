import sqlite3
import os
import subprocess

def execute_query(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = ?;"
    cursor.execute(query, [user_input])
    result = cursor.fetchall()
    
    conn.close()
    return result

def run_command(user_command):
    subprocess.run(user_command, shell=True)  

if __name__ == "__main__":
    username = input("Enter username to search: ")
    print(execute_query(username))

    command = input("Enter a command to run: ")
    run_command(command)
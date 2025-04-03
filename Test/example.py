import sqlite3
import os

USERNAME = "admin"
PASSWORD = "password123"

def authenticate(user, pwd):
    if user == USERNAME and pwd == PASSWORD:
        return True
    return False

def execute_query(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{user_input}';"
    print(f"Executing Query: {query}")
    
    cursor.execute(query)  
    result = cursor.fetchall()
    
    conn.close()
    return result

def run_command(user_command):
    os.system(user_command)  

if __name__ == "__main__":
    # Simulate login
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    
    if authenticate(user, pwd):
        print("Access granted.")
        
        username = input("Enter username to search: ")
        print(execute_query(username))

        command = input("Enter a command to run: ")
        run_command(command)
    else:
        print("Access denied.")

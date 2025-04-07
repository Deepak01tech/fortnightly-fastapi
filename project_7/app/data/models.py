from app.data.database import get_connection
from app.schema import User_create,ClientCreate,ProjectCreate# Make sure this import path is correct

 # You need to define this schema



def create_users_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_user(user: User_create):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (user.username, user.email, user.password)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created successfully"}







def create_clients_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS clients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            client_name VARCHAR(255) NOT NULL,
            created_by INT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def insert_client(client: ClientCreate):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO clients (client_name, created_by) VALUES (%s, %s)"
    values = (client.client_name, client.created_by)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Client created successfully"}




 # You need to define this schema

def create_projects_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS projects (
            id INT AUTO_INCREMENT PRIMARY KEY,
            project_name VARCHAR(255) NOT NULL,
            client_id INT NOT NULL,
            created_by INT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_project(project: ProjectCreate):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO projects (project_name, client_id, created_by) VALUES (%s, %s, %s)"
    values = (project.project_name, project.client_id, project.created_by)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Project created successfully"}




from app.data import database
from app import schema
from app.data.database import get_connection

def get_users_from_db():
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users


def get_user_by_id(user_id: int):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def update_user(user_id: int, user: schema.User_create):
    if not get_user_by_id(user_id):
        return {"message": "User not found"}

    conn = database.get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
    values = (user.username, user.email, user.password, user_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated successfully"}


def delete_user(user_id: int):
    if not get_user_by_id(user_id):
        return {"message": "User not found"}

    conn = database.get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deleted successfully"}


def create_user(user: schema.User_create):
    conn = database.get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (user.username, user.email, user.password)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created successfully"}


from app.data.database import get_connection
from app.schema import ClientCreate



def get_client_by_id(client_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM clients WHERE id = %s"
        cursor.execute(query, (client_id,))
        client = cursor.fetchone()
        print("Fetched client:", client)
        return client
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e
    finally:
        cursor.close()
        conn.close()



def get_all_clients():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM clients"
    cursor.execute(query)
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return clients

def update_client(client_id: int, client: ClientCreate):
    if not get_client_by_id(client_id):
        return {"message": "Client not found"}
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE clients SET client_name = %s, created_by = %s WHERE id = %s"
    values = (client.client_name, client.created_by, client_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Client updated successfully"}

def delete_client(client_id: int):
    if not get_client_by_id(client_id):
        return {"message": "Client not found"}
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM clients WHERE id = %s"
    cursor.execute(query, (client_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Client deleted successfully"}
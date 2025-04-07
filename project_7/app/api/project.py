from app.data import database
from app.schema import ProjectCreate


def get_project_by_id(project_id: int):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM projects WHERE id = %s"
    cursor.execute(query, (project_id,))
    project = cursor.fetchone()
    cursor.close()
    conn.close()
    return project


def get_all_projects():
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM projects"
    cursor.execute(query)
    projects = cursor.fetchall()
    cursor.close()
    conn.close()
    return projects


def update_project(project_id: int, project: ProjectCreate):

    if not get_project_by_id(project_id):
        return {"message": "Project not found"}

    conn = database.get_connection()
    cursor = conn.cursor()
    query = """
        UPDATE projects
        SET project_name = %s, client_id = %s, created_by = %s
        WHERE id = %s
    """
    values = (project.project_name, project.client_id, project.created_by, project_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Project updated successfully"}


def delete_project(project_id: int):
    if not get_project_by_id(project_id):
        return {"message": "Project not found"}
    conn = database.get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM projects WHERE id = %s"
    cursor.execute(query, (project_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Project deleted successfully"}

import requests
import sqlite3
DB_PATH = "app.db"

DB_URL = "http://localhost:6000"
requests.post(DB_URL + "/db/create_user")
def create_user(username, password_hash):
    payload = {"username": username, "password": password_hash}
    res = requests.post(DB_URL + "/db/create_user", json=payload)
    return res.json()

def fetch_user(username):
    res = requests.post(DB_URL + "/db/get_user", json={"username": username})
    if res.status_code == 200:
        return res.json()
    return None

# New functions for image handling to match db_app.py routes
# def upload_image_to_db(username, file_obj):
#     files = {"file": (file_obj.filename, file_obj.stream.read())}
#     data = {"username": username}
#     res = requests.post(DB_URL + "/db/upload_image", data=data, files=files)
#     return res.json()
def upload_image_to_db(username, file, doc_type):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            INSERT INTO images (username, doc_type, filename, filedata)
            VALUES (?, ?, ?, ?)
        """, (username, doc_type, file.filename, file.read()))
        conn.commit()
        return {"status": "success"}

# def fetch_user_images(username):
#     res = requests.post(DB_URL + "/db/list_images", json={"username": username})
#     return res.json()
def fetch_user_images(username, doc_type=None):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        if doc_type:
            cursor.execute("""
                SELECT filename 
                FROM images 
                WHERE username = ? AND doc_type = ?
            """, (username, doc_type))
        else:
            cursor.execute("""
                SELECT filename 
                FROM images 
                WHERE username = ?
            """, (username,))

        rows = cursor.fetchall()
        return [{"filename": r[0]} for r in rows]


# New function to get dummy data
def get_dummy_data_from_db():
    res = requests.get(DB_URL + "/db/get_dummy_data")
    return res.json()

def init_image_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                doc_type TEXT NOT NULL,
                filename TEXT NOT NULL,
                filedata BLOB NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

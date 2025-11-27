import requests

DB_URL = "http://localhost:6000"

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
def upload_image_to_db(username, file_obj):
    files = {"file": (file_obj.filename, file_obj.stream.read())}
    data = {"username": username}
    res = requests.post(DB_URL + "/db/upload_image", data=data, files=files)
    return res.json()

def fetch_user_images(username):
    res = requests.post(DB_URL + "/db/list_images", json={"username": username})
    return res.json()

# New function to get dummy data
def get_dummy_data_from_db():
    res = requests.get(DB_URL + "/db/get_dummy_data")
    return res.json()

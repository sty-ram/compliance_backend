# from flask import Flask
# from flask_cors import CORS
# from controllers.auth_controller import auth
# from controllers.mapping_controller import mapping
# from controllers.image_controller import images



# app = Flask(__name__)
# app.secret_key = "your_secret_key"
# from flask_cors import CORS

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# CORS(app,
#     supports_credentials=True,
#     resources={r"/*": {"origins": [
#         "http://127.0.0.1:8000",
#         "http://localhost:8000",
#         "http://127.0.0.1:8080",
#         "http://localhost:8080"
#     ]}}
# )



# app.register_blueprint(auth)
# app.register_blueprint(mapping)
# app.register_blueprint(images)
# if __name__ == "__main__":
#     app.run(port=5000, debug=True)
    
from flask import Flask
from flask_cors import CORS

from controllers.auth_controller import auth
from controllers.mapping_controller import mapping
from controllers.image_controller import images
from services.db_service import init_image_table
init_image_table()

app = Flask(__name__)
app.secret_key = "your_secret_key"
print("APP INSTANCE:", id(app))

# GLOBAL CORS FIX – Applies to all routes
CORS(app, supports_credentials=True)

# Register blueprints AFTER app + CORS initialized
app.register_blueprint(auth)
app.register_blueprint(mapping)
app.register_blueprint(images)

if __name__ == "__main__":
    @app.after_request

    def debug_cors(response):

        print("CORS HEADER:", response.headers.get("Access-Control-Allow-Origin"))
        return response

    app.run(port=5000, debug=True)
    

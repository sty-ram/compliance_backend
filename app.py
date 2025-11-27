from flask import Flask
from flask_cors import CORS
from controllers.auth_controller import auth
from controllers.mapping_controller import mapping
from controllers.image_controller import images



app = Flask(__name__)
app.secret_key = "your_secret_key"
CORS(app,
    supports_credentials=True,
    resources={r"/*": {"origins": ["http://127.0.0.1:8000"]}}
)


app.register_blueprint(auth)
app.register_blueprint(mapping)
app.register_blueprint(images)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
    

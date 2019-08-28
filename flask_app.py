
# A very simple Flask Hello World app for you to get started with...
import os
os.environ['FLASK_ENV'] = 'development'

from app import app, db
from app.models import User, Post

# app = create_app()

@app.shell_context_processor
def shell_context():
    return {"db": db, "User": User, "Post": Post}


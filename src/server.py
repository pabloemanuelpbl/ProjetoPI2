import os
from dotenv import load_dotenv
from application import app

load_dotenv()

SERVER_PORT = os.getenv("SERVER_PORT")

if __name__ == "__main__":
    app.run( 
        debug=True,
        port=SERVER_PORT,
        host='0.0.0.0'
    )

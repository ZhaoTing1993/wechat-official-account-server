from app import app
import os

port = int(os.getenv('PORT', '5000'))
debug = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
host = os.getenv('HOST', '127.0.0.1')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)

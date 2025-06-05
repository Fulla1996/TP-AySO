import socket
from flask import Flask, request ,jsonify

app = Flask(__name__)

@app.route('/getip', methods=['GET'])
def getip():
        url = request.args.get('url')
        try:
            return socket.gethostbyname(url), 200
        except socket.gaierror:
            return jsonify({"mensaje" : "Error"}), 404

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)

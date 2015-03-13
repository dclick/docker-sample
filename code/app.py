from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
import json
import subprocess
import sys
import getopt
import sqlite3
import os
import time

app = Flask(__name__)
version = "VERSION"

@app.route('/version', methods=['GET'])
def read_hook():
    if request.method == 'GET':
        return Response(json.dumps(time.strftime("%H:%M:%S") + " # " + version), mimetype='application/json')

def main(argv):
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

if __name__ == '__main__':
    main(sys.argv[1:])

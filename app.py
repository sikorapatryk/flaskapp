from flask import Flask, jsonify, make_response
from datetime import datetime
from flask_cors import CORS
import platform
import os
import json_logging
import logging
import sys


app = Flask(__name__)
CORS(app)
json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)
port = int(os.environ.get("FLASK_RUN_PORT", 5000))
env = os.environ.get("FLASK_ENV", 'production')

# init the logger
logger = logging.getLogger("console-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

@app.route('/api/info', methods=['GET'])
def get_info():
    hostname=platform.node()
    logger.info("log with hostname", extra={'props': {"hostname": hostname }})
    return jsonify({'hostname': hostname, 'port': str(port), 'env': str(env) })

@app.route('/api/date', methods=['GET'])
def get_date():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("%H:%M:%S")
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return jsonify({'time': time, 'day': day, 'month': month, 'year':year, 'date_time': date_time})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

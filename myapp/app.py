from flask import Flask
import logging, json

#Basic config of flask and logging
app = Flask(__name__)

LOGS = "./logs/flask_logs.log"

logging.basicConfig(filename=LOGS,
                    filemode='a',
                    format=logging.BASIC_FORMAT,
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Flask Dockerized\n'

@app.route('/logs')
def get_logs():
    data = {}

    with open(LOGS, "r") as f:
        for line in f.readlines():
            if "- -" in line:
                parts = line.split(" ")
                r = parts[-4]

                if r in data:
                    data[r] = data[r] + 1
                else:
                    data[r] = 1


    return json.dumps(data)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

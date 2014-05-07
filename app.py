from flask import Flask, render_template
app = Flask(__name__)
import json
import time

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data.json')
def data():
    with open('contributions_calendar_data.json') as f:
        data = json.loads(f.read())
    # Covert the list of lists github gives us to a dict with timestamps

    timeobj = {}

    for item in data:
        timeStamp = time.strptime(item[0],'%Y/%m/%d')
        timeStamp = time.mktime(timeStamp)
        timeobj[timeStamp] = item[1]

    return json.dumps(timeobj)

if __name__ == '__main__':
    app.run(debug=True)
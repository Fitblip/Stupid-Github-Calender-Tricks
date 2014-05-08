from flask import Flask, render_template, url_for
app = Flask(__name__)
import json
import time
import urllib

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data.json')
def data():
    with open('contributions_calendar_data.json') as f:
        data = json.loads(f.read())
    # Covert the list of lists github gives us to a dict with timestamps

@app.route('/<username>/calender')
def userCalander(username):
    return render_template('index.html',dataSource=url_for('data',username=username))


@app.route('/<username>/data.json')
def data(username):
    data = urllib.urlopen('https://github.com/users/%s/contributions_calendar_data' % username).read()

    data = json.loads(data)

    timeobj = {}

    for item in data:
        timeStamp = time.strptime(item[0],'%Y/%m/%d')
        timeStamp = time.mktime(timeStamp)
        timeobj[timeStamp] = item[1]

    return json.dumps(timeobj)

if __name__ == '__main__':
    app.run(debug=True)
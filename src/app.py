from flask import Flask
from flask import jsonify

app = Flask(__name__)
requ = ""


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def doRequest(path):
    requ = +path + ' \n'
    with open("test.txt", "a") as myfile:
        myfile.write(requ)
    return "None"


@app.route('/server-d/get')
def get():
    with open("test.txt", "r") as infile:
        return 'we have something: ' + '\n '.join(infile.readlines())


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=6000)

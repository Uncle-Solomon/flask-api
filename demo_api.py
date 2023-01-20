from flask import Flask, json, render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    text = "'Go to /all to see all events'"

    return render_template('index.html', html_text = text)

@app.route("/all")
def all():
    json_uri = os.path.join("data", "data.json")
    data_json = json.load(open(json_uri))

    #jsonify or json.dumps
    #return json.dumps(data_json)


    return render_template('index.html', html_text = data_json)


if __name__ == "__main__":
    app.run(debug=True)




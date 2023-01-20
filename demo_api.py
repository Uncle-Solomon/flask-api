from flask import Flask, json, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def hello():
    text = "'Go to /all to see all events'"

    return render_template('index.html', html_text = text)

@app.route("/all")
def all():
    json_url = os.path.join("data", "data.json")
    data_json = json.load(open(json_url))

    #jsonify or json.dumps
    #return json.dumps(data_json)


    return render_template('index.html', html_text = data_json)

@app.route("/year/<year>", methods=['GET', 'POST'])
def add_year(year):

    json_url = os.path.join("data","data.json")
    data_json = json.load(open(json_url))
    data = data_json["events"]
    if request.method == 'GET':
        data_json = json.load(open(json_url))
        data = data_json['events']
        year = request.view_args['year']

        output_data = [x for x in data if x['year']==year]
        
     
        return render_template('events.html',html_text=output_data)    

    # return render_template('index.html', html_text = data)

@app.route("/add", methods=['GET', 'POST'])
def form():
        if request.method == "GET":
            return render_template('forms.html')

        elif request.method == 'POST':
            json_url = os.path.join("data","data.json")
            # year = request.form['year']
            year = 2023
            id = 3

            # id = request.form['ID']
            category = request.form['category']
            event = request.form['event']
            event_yr= { "year":year,
                        "id":id,
                        "event_category":category,
                        "event":event
                        }

            with open(json_url,"r+") as file:
                data_json = json.load(file)
                data_json["events"].append(event_yr)
                json.dump(data_json, file)
            
            #Adding text
            text_success = "Data successfully added: " + str(event_yr)
            return redirect('index.html', html_text=text_success)
# @app.route("/add", methods=['POST'])
# def form_submit():


if __name__ == "__main__":
    app.run(debug=True)




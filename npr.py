#import flask and makes the templates
from flask import Flask, render_template, redirect, url_for
#import your python dict using the variable you made in nprlist.py
from nprlist import PEOPLE
app = Flask(__name__)



#this retrieves the ids AND the names from the data and adds it to the list
def get_ids_and_names(source):
    ids_and_names = []
    for row in source:
        id = row["id"]
        name = row["Name"]
        ids_and_names.append( [id, name] )
            #RETURN LINE HAS TO BE TABBED JUST RIGHT. IF IT ISNT INDENTED, THE LOOP WILL NOT WORK. THIS ONE NEEDS TO BE PARALLEL TO THE FOR ROW IN SOURCE LINE
    return ids_and_names

def get_people(source, id):
    for row in source:
        if id == str(row["id"]):
            name = row["Name"]
            program = row["Program"]
            birthplace = row["Birthplace"]
            id = str(id)
            #RETURN LINE HAS TO BE TABBED JUST RIGHT. IF IT ISNT INDENTED, THE LOOP WILL NOT WORK. THIS ONE HAS TO BE PARALLEL TO THE ID=STR(ID). I DONT KNOW WHY BUT IT JUST WORKS
            return id, name, program, birthplace


#this is the route for the homepage of the site.
@app.route('/')
@app.route('/index/')
def index():
    ids_and_names = get_ids_and_names(PEOPLE)
    return render_template('index.html', pairs=ids_and_names)

#route for the detail pages
@app.route('/people/<id>')
def people(id):
    id, name, program, birthplace = get_people(PEOPLE, id)
    return render_template('people.html', name=name, program=program, birthplace=birthplace)


#run in debug mode
if __name__ == '__main__':
    app.run(debug=True)

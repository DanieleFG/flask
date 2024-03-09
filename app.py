from flask import Flask, render_template
import urllib.request, json


app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"

    response = urllib.request.urlopen(url)
    data = response.read()
    disct = json.loads(data)

    return render_template("charscters.html", characters=disct['results'])

@app.route("/personagem/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id

    response = urllib.request.urlopen(url)
    data = response.read()
    disct = json.loads(data)

    return render_template("profile.html", profile=disct)


@app.route("/lista")

# def hellow_world():
#     return '<h1>Olá DAny!!!</h1>'

def get_list_element():
    url = "https://rickandmortyapi.com/api/character/"

    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name" : character["name"],
            "status" : character["status"]
        }

        characters.append(character)
    return {"characters" : characters}

@app.route("/locations")
def get_list_locations():
    url = 'https://rickandmortyapi.com/api/location'
    response = urllib.request.urlopen(url)
    location = response.read()
    disc= json.loads(location)

    return render_template("locations.html", location = disc['results'])


@app.route("/location/<id>")
def get_list_location(id):
    url = 'https://rickandmortyapi.com/api/location/' + id
    response = urllib.request.urlopen(url)
    location = response.read()
    disc= json.loads(location)

    return render_template("location.html", location = disc)





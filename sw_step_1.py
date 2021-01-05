import requests
from pprint import pprint
import random


from flask import Flask, render_template

app = Flask(__name__)



def get_character():
    character1 = random.randint(1, 88)

    url = 'https://swapi.co/api/people/' + str(character1) + '/'

    response = requests.get(url)

    return response.json()




def get_character2(battle_character):
    character2 = random.randint(1, 88)
    while battle_character == character2:
        character2 = random.randint(1, 88)

    url2 = 'https://swapi.co/api/people/' + str(character2) + '/'

    response2 = requests.get(url2)

    return response2.json()



def heightoutcome(battle_character, opponent_character):
    if battle_character["height"] >= opponent_character["height"]:
        return'You win!'
    else:
        return 'You lose'



def filmoutcome(battle_character, opponent_character):
    if len(battle_character["films"]) >= len(opponent_character["films"]):
        return'You win!'
    else:
        return 'You lose'


def weightoutcome(battle_character, opponent_character):
    if battle_character['mass'] == "unknown":
        battle_mass = 0
    else: battle_mass = float(battle_character['mass'])

    if opponent_character['mass'] == "unknown":
        opponent_mass = 0
    else: opponent_mass = float(opponent_character['mass'])

    if battle_mass >= opponent_mass:
        return'You win!'
    else:
        return 'You lose'






@app.route('/')
def show_character():
    battle_character = get_character()
    opponent_character = get_character2(battle_character)
    weight_outcome = weightoutcome(battle_character, opponent_character)
    height_outcome = heightoutcome(battle_character, opponent_character)
    film_outcome = filmoutcome(battle_character, opponent_character)

    name1 = str(battle_character['name'])
    height1 = str(battle_character['height'])
    weight1 = str(
        battle_character['mass'])
    films1 = str(len(battle_character['films']))
    name2 = str(
        opponent_character['name'])
    height2 = str(opponent_character['height'])
    weight2 = str(
        opponent_character['mass'])
    films2 = str(len(opponent_character['films']))
    weightout = str(
        weight_outcome)
    heightout = str(height_outcome)
    filmout = str(film_outcome)



    return render_template('Style.html', name1=name1, height1=height1, weight1 =weight1, films1 =films1, name2=name2, height2=height2, weight2 = weight2, films2 = films2, weightout = str(weight_outcome), heightout = str(height_outcome), filmout = str(film_outcome))


app.run(debug=True)









#
#
# char1weight = character1der['mass']
# if char1weight == "unknown":
#     char1weight = 0
# else :
#     char1weight = int(character1der["mass"])
# char1films = len(character1der['films'])
# char1height = int(character1der['height'])
#
#
#
# character2 = random.randint(1, 88)
# while character1 == character2:
#     character2 = random.randint(1, 88)
#
#
# url2 = 'https://swapi.co/api/people/' + str(character2) + '/'
#
# response2 = requests.get(url2)
#
# character2der = response2.json()
#
# pprint('Your opponent is ' + str(character2der['name']))
# pprint('Their height is ' + str(character2der['height']) + ' cm.')
# pprint('Their weight is ' + str(character2der['mass']) + ' kg.')
# pprint('They have been in ' + str(len(character1der['films'])) + ' film(s).')
#
# char2weight = character2der['mass']
# if char2weight == "unknown":
#     char2weight = 0
# else :
#     char2weight = int(character2der["mass"])
#
# char2height = int(character2der['height'])
# char2films = len(character2der['films'])
#
#
# if metric == 'height' and char1height >= char2height:
#     print('You win!')
# elif metric == 'weight' and char1weight >= char2weight:
#     print('You win!')
# elif metric == 'films' and char1films >= char2films:
#     print('You win!')
# else:
#     print('You lose!')
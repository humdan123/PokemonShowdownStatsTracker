import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
spreadsheet = client.open("Gen 7 Draft League")
NAME, GAME, KILL, DEATH = 2, 3, 4, 5


def add_death(pokemon, player_name):
    player_sheet = find_player_sheet(player_name)
    name_val = find_pokemon(pokemon, player_sheet)
    death_val = player_sheet.cell(name_val, DEATH).value
    player_sheet.update_cell(name_val, DEATH, int(death_val)+1)

def add_kill(pokemon, player_name):
    player_sheet = find_player_sheet(player_name)
    name_val = find_pokemon(pokemon, player_sheet)
    kill_val = player_sheet.cell(name_val, KILL).value
    player_sheet.update_cell(name_val, KILL, int(kill_val)+1)


def add_game(pokemon, player_name):
    
    player_sheet = find_player_sheet(player_name)
    name_val = find_pokemon(pokemon, player_sheet)
    game_val = player_sheet.cell(name_val, GAME).value
    player_sheet.update_cell(name_val, GAME, int(game_val)+1)



def find_pokemon(pokemon, player_sheet):
    pokemons = player_sheet.col_values(2)
    if "-Mega" in pokemon:
        pokemon = pokemon[:-5]
    for i in range(len(pokemons)):
        print((pokemon, pokemons[i]))
        if pokemons[i] == pokemon:
            return i + 1
    return add_new_pokemon(pokemon, player_sheet, len(pokemon))

def find_player_sheet(player_name):
    return spreadsheet.worksheet(player_name)

def add_new_pokemon(pokemon, player_sheet, i):
    
    player_sheet.update_cell(i+1, NAME, pokemon)
    player_sheet.update_cell(i+1, GAME, 0)
    player_sheet.update_cell(i+1, KILL, 0)
    player_sheet.update_cell(i+1, DEATH, 0)


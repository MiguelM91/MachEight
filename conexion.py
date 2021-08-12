import requests
import json

entry = int(input("Escriba la altura a buscar en pulgadas: \n"))
output = []

# Conección a la API
def Connection_Validation():

    if __name__ == '__main__' :
        url = 'https://mach-eight.uc.r.appspot.com/'
        response = requests.get(url)
# Quiero poner un try catch

    if response.status_code == 200:
        content = response.content
        file = open('info.json','wb')
        file.write(content)
        file.close
    else:
        print("Connection Error")

Connection_Validation()

# Leer archivo e imprimir data

def Reading_Printing_Data():
    f = open("info.json","r")
    content = f.read()
    jsondecoded = json.loads(content)

    for player in jsondecoded["values"]:
        playerName = player["first_name"]
        hightIn = int(player["h_in"])
        hightMeters = float(player["h_meters"])
        playerLastName = player["last_name"]
        
        if entry == hightIn:
            print(playerName, playerLastName)

Reading_Printing_Data()

       
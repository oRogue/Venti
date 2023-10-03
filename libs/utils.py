import os
import requests
import dotenv
dotenv.load_dotenv() # Loads .env file

RIOT = str(os.getenv("RIOT")) # Riot API key

def clearNameSpaces(nameWithSpaces):
    result = ""
    for n in nameWithSpaces:
        result = result + "" + str(n)
    return result

def getProfile(region, name):
    if region == "sg":
        API_Riot = "https://sg2.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + RIOT
    response = requests.get(API_Riot)
    jsonDataSummoner = response.json()
    sEncryptedId = jsonDataSummoner['id']
    sName = jsonDataSummoner['name']
    sLevel = "Lvl. " + str(jsonDataSummoner['summonerLevel'])
    sIcon = "http://ddragon.leagueoflegends.com/cdn/12.13.1/img/profileicon/" + str(jsonDataSummoner['profileIconId']) + ".png"
    return (sName, sLevel, sIcon, sEncryptedId)

def getRanks(region, sEncryptedId):
    if region == "sg":
        API_Riot = "https://sg2.api.riotgames.com/lol/league/v4/entries/by-summoner/" + sEncryptedId + "?api_key=" + RIOT
    response = requests.get(API_Riot)
    jsonDataSummoner = response.json()
    calls = {0:"queueType", 1:"tier", 2:"rank", 3:"leaguePoints", 4:"wins", 5:"losses"}
    ranks = []
    try:
        for i in range(3):
            for j in range(6):
                ranks.append(jsonDataSummoner[i][calls[j]])
    except:
        pass
    return ranks
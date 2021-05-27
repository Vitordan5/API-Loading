import requests
import ast

def cepCoord(cep):
    url="https://www.cepaberto.com/api/v3/cep?cep="+cep

    headers = {'Authorization': 'Token token=20c49238532d724e19f6731315e70ce2'}
    response = requests.get(url, headers=headers)
    tx = str(response.json())

    valor = ast.literal_eval(tx)
    lat = valor['latitude']
    long= valor['longitude']
    localizacao=[]
    localizacao.append(lat)
    localizacao.append(long)
    return localizacao



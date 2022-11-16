import requests

response = requests.get('https://api.pokemontcg.io/v2/cards')

print(response.json())
print(response.status_code)
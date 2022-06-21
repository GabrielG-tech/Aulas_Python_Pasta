# pip install requests
import requests
# https://code-battle-lac.herokuapp.com/api-docs
api_url = "https://code-battle-lac.herokuapp.com"

# post /signin
user = requests.post(api_url + "/signin", json = {
    "email": "gabriel.gsouza@al.infnet.edu.br",
    "password": "987654321"
})

user = user.json()
user_token = user['token']
headers = {
    'Authorization': f'Bearer {user_token}'
}

field = 'LCA22T2M1'
# game = requests.get(api_url + "/games/" + field + '/add/me', headers=headers)
#game = requests.post(api_url + "/games", headers=headers, json = {'field': field})

# action = requests.get(api_url + "/games/" + field + "/move/" + 'n', headers=headers)
action = requests.get(api_url + "/games/" + field + "/attack/" + 'n', headers=headers)

#       N
#   NW  |  NE
# W ----+---- E
#   SW  |  SE
#       S

print(action.json())
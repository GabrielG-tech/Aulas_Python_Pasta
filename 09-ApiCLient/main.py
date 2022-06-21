# pip install requests
import requests
# https://code-battle-lac.herokuapp.com/api-docs
api_url = "https://code-battle-lac.herokuapp.com"

# post /signin
res = requests.post(api_url + "/signin", json = {
    "email": "gabriel.gsouza@al.infnet.edu.br",
    "password": "gabriel.gsouza"
})

# post /update_pass
# res = requests.post(api_url + "/update_pass")

print(res)
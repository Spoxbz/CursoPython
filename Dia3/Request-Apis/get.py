import requests

url = "http://localhost:8081/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
    
# msfadmin
# msfadmin
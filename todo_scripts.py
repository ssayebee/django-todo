import requests

base_url = 'http://127.0.0.1:8000/todo/'
urls = {
    'login': base_url + 'auth/login/',
    'todos': base_url + 'todos/'
}

client = requests.session()

# Retrieve the CSRF token first
client.get(urls['login'])  # sets cookie
if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']
else:
    csrftoken = client.cookies['csrf']

res = client.post(urls['login'], data = {'next': '/todo/todos', 'csrfmiddlewaretoken': csrftoken, 'username': 'justin', 'password': 'password'})
print(res.status_code)

print(res.text)

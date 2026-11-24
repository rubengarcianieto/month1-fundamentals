import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(type(r))
print([name for name in dir(r) if not name.startswith("_")])

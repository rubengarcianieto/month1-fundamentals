import requests

new_post = {"title": "orchestration test", "body": "content example", "userId": 1}

r = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
print(r.status_code)  # 201 expected
print(r.json())

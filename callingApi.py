import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

print(f"Fetched {len(posts)} posts.")
print("First post title:", posts[0]["title"])

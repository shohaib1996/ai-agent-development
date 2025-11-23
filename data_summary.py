import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

# print(f"Posts: {posts}")

user_post_count = {}

for post in posts:
    user_id = post["userId"]
    if user_id in user_post_count:
        user_post_count[user_id] += 1
    else:
        user_post_count[user_id] = 1

result = [
    {"userId": user_id, "count": count} for user_id, count in user_post_count.items()
]
with open("posts_summary.json", "w") as f:
    json.dump(result, f, indent=4)

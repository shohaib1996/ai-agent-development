# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("sample.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

# with open("output.txt", "w") as f:
#     f.write("Hello world")

# with open("output.txt", "a") as f:
#     f.write("\nNew line added")

# with open("sample.txt", "r") as f:
#     text = f.read()
#     words = text.split()
#     print("File sample.txt has", len(words), "words.")

# import json

# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)

# user = {"name": "Shohaib", "age": 28, "skills": ["Python", "AI", "Agents"]}

# with open("user.json", "w") as f:
#     json.dump(user, f, indent=4)

# json_str = '{"name": "Alex", "age": 30}'
# data = json.loads(json_str)
# print(data)
# import os

# if os.path.exists("sample.txt"):
#     print("File exists")
# else:
#     print("File not found")


def process(line):
    print(f"Processing: {line.strip()}")


with open("sample.txt", "r") as f:
    for line in f:
        process(line)

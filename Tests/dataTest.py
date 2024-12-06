import json

with open("data/database.json", "r", encoding="utf-8") as file:
    # Parse the JSON file into a Python dictionary
    data = json.load(file)

# Access the "users" list
users = data.get("users", [])

# Iterate through the list and print each username
for user in users:
    print(user.get("username"))

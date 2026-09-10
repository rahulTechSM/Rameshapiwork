from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["PYWork"]

# Test connection
client.admin.command("ping")
print("MongoDB connected")


users = db["users"]
users.insert_one({
    "name": "Rahul",
    "age": 30,
    "email": "rahul@gmail.com"
})
users.insert_many([
    {"name": "Amit", "age": 28},
    {"name": "Neha", "age": 25}
])
for user in users.find():
    print(user)


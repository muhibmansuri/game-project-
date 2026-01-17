import json

# Ek complex data structure lete hain taaki fark saaf dikhe
data = {
    "student_id": 101,
    "info": {
        "name": "Muhib",
        "hobbies": ["Coding", "Reading", "Gaming"]
    },
    "is_active": True
}

print("=== Case 1: Bina Indent ke (Default) ===")
# Jab hum indent nahi dete, toh poora data ek hi line mein aata hai.
flat_json = json.dumps(data)
print(flat_json)

print("\n=== Case 2: indent=2 ke saath ===")
# Har level pe 2 spaces ka gap hoga. Thoda compact dikhta hai.
json_2 = json.dumps(data, indent=2)
print(json_2)

print("\n=== Case 3: indent=4 ke saath ===")
# Har level pe 4 spaces ka gap hoga (Standard style).
# Notice karo kaise 'info' ke andar 'hobbies' aur andar gaya hai.
json_4 = json.dumps(data, indent=4)
print(json_4)

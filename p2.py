transactions = [
    {"user_id": 1, "amount": 500, "type": "credit", "timestamp": "2024-01-01 10:00:00", "status": "completed"},
    {"user_id": 1, "amount": 200, "type": "debit", "timestamp": "2024-01-01 11:00:00", "status": "completed"},
    {"user_id": 1, "amount": 100, "type": "debit", "timestamp": "2024-01-01 11:05:00", "status": "failed"},
    {"user_id": 2, "amount": 1000, "type": "credit", "timestamp": "2024-01-01 10:30:00", "status": "completed"},
    {"user_id": 2, "amount": 1200, "type": "debit", "timestamp": "2024-01-01 11:30:00", "status": "completed"},
    {"user_id": 2, "amount": 300, "type": "credit", "timestamp": "2024-01-01 12:00:00", "status": "completed"},
]



balances = {}

for t in transactions:
    if t["status"] != "completed":
        continue

    user = t["user_id"]

    if user not in balances:
        balances[user] = 0

    if t["type"] == "credit":
        balances[user] += t["amount"]
    else:
        balances[user] -= t["amount"]

print("Final Balances:")
for user, balance in balances.items():
    print(f"User {user}: ₹{balance}")


print("\nSuspicious Users:")

users = {}

for t in transactions:
    user = t["user_id"]

    if user not in users:
        users[user] = {
            "credit": 0,
            "debit": 0,
            "count": 0,
            "max_debit": 0
        }

    if t["status"] == "completed":

        if t["type"] == "credit":
            users[user]["credit"] += t["amount"]

        if t["type"] == "debit":
            users[user]["debit"] += t["amount"]

            if t["amount"] > users[user]["max_debit"]:
                users[user]["max_debit"] = t["amount"]

        users[user]["count"] += 1

for user, data in users.items():

    suspicious = False

    # Rule 1
    if data["debit"] > data["credit"]:
        suspicious = True

    # Rule 2
    if data["count"] > 3:
        suspicious = True

    # Rule 3
    if data["credit"] > 0 and data["max_debit"] > 0.7 * data["credit"]:
        suspicious = True

    if suspicious:
        print("User", user)



latest = {}

for t in transactions:

    if t["status"] != "completed":
        continue

    user = t["user_id"]

    if user not in latest:
        latest[user] = t
    elif t["timestamp"] > latest[user]["timestamp"]:
        latest[user] = t

print("\nLatest Valid Transactions:")

for user, transaction in latest.items():
    print(f"User {user}: {transaction}")
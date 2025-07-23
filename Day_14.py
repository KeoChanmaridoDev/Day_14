from Data import data
from ascii import art, art_
import random
print (art)

# for i in data:
#     print(i)


def account(account):
    account_name = account["name"]
    account_country = account["country"]
    account_description = account["description"]
    return f"{account_name}, {account_description}, {account_country} "

def check_answer(user, a_value, b_value):
    if a_value > b_value:
        return user =="A"
    else:
        return user == "B"

game_end = True
b = random.choice(data)

while game_end:
    win_count = 0
    a = b
    print(f"Compare A: {account(a)}")
    a_value_follower  = a["follower_count"]


    print (art_)

    b = random.choice(([item for item in data if item != a]))
    print(f"Compare B: {account(b)}")
    b_value_follower = b["follower_count"]

    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    print("\n" * 20)

    is_correct = check_answer(user, a_value_follower, b_value_follower)
    if is_correct:
        win_count += 1
        print(f"Correct!, You have {win_count}.")
    else:
        print(f"Incorrect!.")
        game_end = False





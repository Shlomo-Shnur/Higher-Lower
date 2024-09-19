import art
import game_data
import random

LOGO = art.logo
VS = art.vs
DATA_LIST = game_data.data


def more_followers(choice_1, choice_2):
    if choice_1["follower_count"] > choice_2["follower_count"]:
        return "a"
    elif choice_1["follower_count"] < choice_2["follower_count"]:
        return "b"
    else:
        return "BOTH"


def play():
    choices = random.choices(DATA_LIST, k=2)
    choice_one = choices[0]
    choice_two = choices[1]
    score = 0
    print("\n" * 20)
    print(LOGO)
    while True:
        print(f"Compare A: {choice_one["name"]}, a {choice_one["description"]}, from {choice_one["country"]}")
        print(VS)
        print(f"Against B: {choice_two["name"]}, a {choice_two["description"]}, from {choice_two["country"]}")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        real_answer = more_followers(choice_one, choice_two)
        print("\n" * 80)
        print(LOGO)
        if user_answer == real_answer or real_answer == "BOTH":
            score += 1
            print(f"You're right! Current score: {score}.")
            choice_one = choice_two
            while choice_one == choice_two:
                choice_two = random.choice(DATA_LIST)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return


if __name__ == "__main__":
    play()

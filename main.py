import game_data
import game_data as gd
import art as art
import random

print(art.logo)


def random_number():
    NUMBER = random.randint(1, 50)
    return NUMBER

game_state = True
print("Welcome to higher or lower")
a = random_number()
b = random_number()
while game_state == True:
    b = random_number()
    first = game_data.data[a]
    second = game_data.data[b]
    print(f"Random number genreated:{a}, {b}\n")
    first_follower = game_data.data[a]['follower_count']
    second_follower = game_data.data[b]['follower_count']
    print(f"Follower count for a: {first_follower}, "
          f"and b: {second_follower}\n")

    print(f"First choice is: {first['name']}, occupation is {first['description']}, and they are "
          f"from the {first['country']}\n")
    print(f"Second choice is:  {second['name']}, occupation is {second['description']}, and they are "
          f"from the {second['country']}\n")
    choice = int(input("Who has more followers, 1 or 2"))

    if choice == 1:
        if first_follower > second_follower:
            print("correct!")


        else:
            print("incorrect")
            game_state = False
    if choice == 2:
        if second_follower > first_follower:
            print("correct!")
            a = b

        else:
            print("incorrect")
            game_state = False



print("game over shitter")

# print("higher or lower game")
# followers = 0
# for i in data:
#     followers += i["follower_count"]
#
# print(followers)

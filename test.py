# import requests

# advice = requests.get("https://fun-api.sujalgoel.engineer/advice").json()["advice"]
# print("\33[1m" + "Advice: " + "\33[0m" + "\33[92m" + advice + "\33[0m")

# import pyautogui
# pyautogui.hotkey('alt', 'f4')

# import random

# while True:
#     low = random.randint(0, 500)
#     up = random.randint(500, 1000)
#     main = random.randint(low, up)
#     print("The number is chosen and you only have 6 chances to guess that number.")
#     live = 6
#     guesses = 0
#     while guesses < live:
#         guesses += 1
#         try:
#             guess = int(input("Enter your guess : "))
#         except ValueError:
#             guess = int(input("Enter your guess : "))
#         if guess == main:
#             print("Congratulations, you have won the game in", guesses, "guess(es).")
#             ans = input("Do you want to play again (y/n) : ")
#             break
#         elif guess < main:
#             print(
#                 "The number is bigger than",
#                 guess,
#                 "\nYou have",
#                 6 - guesses,
#                 "lives left.",
#             )
#         elif guess > main:
#             print(
#                 "The number is smaller than",
#                 guess,
#                 "\nYou have",
#                 6 - guesses,
#                 "lives left.",
#             )
#     if guesses >= 6:
#         print(
#             "It seems that you run out of lives.\nThe number which was guessed is", main
#         )
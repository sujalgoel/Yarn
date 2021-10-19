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

# import random

# while True:
#     print("\33[93m" + "\33[1m" + f"How many chances do you want?" + "\33[0m" + "\n")
#     try:
#         live = int(input())
#     except ValueError:
#         continue
#     win = False
#     guesses = 0
#     num = random.randint(0, 1000)
#     print(
#         "\33[93m"
#         + "\33[1m"
#         + f"The number is chosen and you only have {live} chances to guess that number."
#         + "\33[0m"
#         + "\n"
#     )
#     while guesses < live:
#         try:
#             guess = int(input("Enter your guess: "))
#             guesses += 1
#         except ValueError:
#             continue
#         if guess == num:
#             print(
#                 "\33[92m"
#                 + "\33[1m"
#                 + "\nCongratulations, you have won the game in "
#                 + "\33[0m"
#                 + "\33[91m"
#                 + "\33[1m"
#                 + str(guesses)
#                 + "\33[0m"
#                 + "\33[92m"
#                 + "\33[1m"
#                 + f" {'guesses' if guesses > 1 else 'guess'}."
#                 + "\33[0m"
#                 + "\n"
#             )
#             win = True
#             break
#         elif guess < num:
#             if (live - guesses) != 0:
#                 print(
#                     "\33[91m"
#                     + "\33[1m"
#                     + "\nThe number is greater than "
#                     + "\33[0m"
#                     + "\33[92m"
#                     + "\33[1m"
#                     + str(guess)
#                     + "."
#                     + "\33[0m"
#                     + "\33[91m"
#                     + "\33[1m"
#                     + " You have "
#                     + "\33[0m"
#                     + "\33[92m"
#                     + "\33[1m"
#                     + str(live - guesses)
#                     + "\33[0m"
#                     + "\33[91m"
#                     + "\33[1m"
#                     + f" {'chances' if (live - guesses) > 1 else 'chance'} left."
#                     + "\33[0m"
#                     + "\n"
#                 )
#         elif guess > num:
#             if (live - guesses) != 0:
#                 print(
#                     "\33[91m"
#                     + "\33[1m"
#                     + "\nThe number is smaller than "
#                     + "\33[0m"
#                     + "\33[92m"
#                     + "\33[1m"
#                     + str(guess)
#                     + "."
#                     + "\33[0m"
#                     + "\33[91m"
#                     + "\33[1m"
#                     + " You have "
#                     + "\33[0m"
#                     + "\33[92m"
#                     + "\33[1m"
#                     + str(live - guesses)
#                     + "\33[0m"
#                     + "\33[91m"
#                     + "\33[1m"
#                     + f" {'chances' if (live - guesses) > 1 else 'chance'} left."
#                     + "\33[0m"
#                     + "\n"
#                 )
#     if guesses >= live:
#         if win is False:
#             print(
#                 "\33[93m"
#                 + "\33[1m"
#                 + "\nIt seems that you ran out of chances. The number which I guessed was "
#                 + "\33[0m"
#                 + "\33[1m"
#                 + str(num)
#                 + "."
#                 + "\33[0m"
#                 + "\n"
#             )

# Welcome to my Magic 8-BallBall Project 🎱, on Codecademy!
# https://www.codecademy.com/journeys/computer-science/paths/cscj-22-intro-to-programming/tracks/cscj-22-introduction-to-computer-science-career-path/modules/cscj-22-python-control-flow/projects/python-magic-8-ball

# In Python, we can use the .randint() function from the "random" module to generate a random number from a range. But first, let’s import this module so we can use its functions.
import random

# In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = "Peter"

# Next, declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
question = "Will I become a software engineer, someday?"

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
answer = ""

# Declare a variable called random_number, and assign it to the function call: random.randint(1, 20) which will generate a random number between 1 (inclusive) and 20 (inclusive).
random_number = random.randint(1, 20)

# Use a list of answers and indexing it with the random number (1-20).
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "All signs point to yes", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]

answer = answers[random_number - 1] if 1 <= random_number <= 20 else "Error"

# Error message, in the event a question isn't provided
if question == "":
  print("If you don't provide a question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!")
# What happens when a name isn't provided
elif name == "":
  print("Question:", question)
else:
  print(name, "asks:", question)

# This if statement prevents a question being answered, when a question was never provided, in the first place.
if question != "":
  print("Magic 8-Ball's Answer:", answer)

# Interested in a laugh, after reading this code?!
# Check out the vid ⬇️
# Hopefully, you'll find the 8-Ball to be like Puddy, in your hands!🤣
# https://youtu.be/qD5Sq761J20?si=dl93FbJkM7w9Hk3J&t=24

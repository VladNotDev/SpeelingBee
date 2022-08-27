# ---- Imports ----
import pyttsx3  # pip install pyttsx3 in terminal
from random_word import RandomWords  # pip install random-word in terminal


# ---- Initialize Stuffs ----
r = RandomWords()
text_speech = pyttsx3.init()


# ---- Global Variables ----

number_of_rounds = 10
score = 0


def SpellRound():
    # Fetch a random word
    word_to_spell = r.get_random_word(hasDictionaryDef="true")
    if word_to_spell == None:
        return SpellRound()

    if word_to_spell:
        word_to_spell = word_to_spell.lower()

    # Tell the player the word using text to speech
    text_speech.say(f"Spell {word_to_spell}")
    text_speech.runAndWait()
    # Ask the player for answer
    player_answer = input("What is your answer? \n").lower()

    # Check if player's answer is right or wrong
    if player_answer == word_to_spell:
        text_speech.say("That is correct")
        text_speech.runAndWait()
        print("\n")
        return 1
    else:
        text_speech.say(f"That is wrong")
        text_speech.runAndWait()
        print(f"Correct Answer is {word_to_spell} \n")
        return 0

# ----- Game Loop ------


for i in range(number_of_rounds):
    score += SpellRound()


text_speech.say(f"Congratulations! You scored {score} out of 10 points")
text_speech.runAndWait()

import random

def update_display_word(dw,sw,g):
    new_display_word = ""

    for k in range(len(sw)):
        if g == sw[k]:
            new_display_word += g
        else:
            new_display_word += dw[k]
    return new_display_word

def main():
    print("Guess My Word")

    word_options = ["pencil","mouse", "human", "computer", "catapult," "winston"]
    secret_word = random.choice(word_options)
    print(secret_word)

    word_length = len(secret_word)
    display_word = "*" * word_length
    print(display_word)

    guessed_letters = []
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Please guess one letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed ",guess, " Try again.")
            continue
        guessed_letters.append(guess)
        display_word = update_display_word(display_word,secret_word,guess)
        print(display_word)
        if display_word == secret_word:
            print("You got it")
            break

main()

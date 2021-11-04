import random
from words import words
from lives_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    # getting the input
    while len(word_letters) > 0 and lives > 0:
        
        # used letters
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # user guess input
        user_input = input('Guess a letter: ').upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
                print('')

            else:
                lives -= 1
                print('\nYour letter,', user_input, 'is not in the word.')

        elif user_input in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died. The word was', word)
        print('RIP!')
    else:
        print('Congratulations! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()

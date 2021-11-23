Linz = '+=+=' * 10
print('Hello, Welcome to Girlfriend trivia!')
print(Linz)

Linz = '+=+=' * 10
answer = input('Are you ready to play? (yes/no): ')
print(Linz)
score = 0
total_q = 4


if answer == 'yes':
    answer = input('1. What is my full name? ')
    if answer == 'Grace Kathryn Foster':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'Grace Kathryn Foster':
    answer = input('2. What is my favorite color? ')
    if answer == 'Blue':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'Blue':
    answer = input('3. What is my favorite foodd? ')
    if answer == 'Pizza':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'Pizza':
    answer = input('4. Who do I love the most? ')
    if answer == 'You':
        score += 1
        print('')
    else:
        print('Ah.. You Silly Goose... I love you! <3')

Linz = '+=+=' * 10
print('\nThank you for participating in this Silly GirlFriend Trivia Game, you got', score, "questions correct.")
you = (score/total_q) * 100

print("You:", str(you) + '%')
print("Bye Bye!")
print(Linz)

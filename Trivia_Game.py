Linz = '+=+=' * 10
print('Hello, Welcome to the Ultimate 4 question Trivia!')
print(Linz)

Linz = '+=+=' * 10
answer = input('Are you ready to play? (yes/no): ')
print(Linz)
score = 0
total_q = 4


if answer == 'yes':
    answer = input('1. Who is Mark Zuckerberg? ')
    if answer == 'A Lizard':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'A Lizard!? Duh!!':
    answer = input('2. What goes on pizza? ')
    if answer == 'Pineapple':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'Pineapple':
    answer = input('3. What make an orange be an orange? ')
    if answer == 'Citrus Red 2':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

if answer == 'Citrus Red 2':
    answer = input('4. What is Gordon Ramseys favorite sauce? ')
    if answer == 'Lamb Sauce':
        score += 1
        print('')
    else:
        print('Ah.. Lamb Sauce, you Idiot!')

Linz = '+=+=' * 10
print('\nThank you for participating in this Silly 4 question Trivia Game, you got', score, "questions correct.")
you = (score/total_q) * 100

print("You:", str(you) + '%')
print("Bye, Bye!")
print(Linz)

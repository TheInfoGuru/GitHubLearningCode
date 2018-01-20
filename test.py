secret = 'justice'
blanks = '_' * len(secret)
guessed = 'eintusljc'
count = 0

for letter in secret:
    if letter in guessed:
        blanks = blanks[:count] + letter + blanks[count + 1:]
    count += 1

for j in blanks:
    print(j, end=' ')

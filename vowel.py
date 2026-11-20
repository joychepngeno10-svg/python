# VOWEL COUNTER
text = (input("enter a word: "))
vowels = 0
for letter in text:
    if letter in "aeiou":
        vowels += 1
        print("vowels:", vowels)


# BIGGEST NUMBER
print("================================")
numbers = [4, 17, 9, 23, 8]
biggest = numbers[0]
for number in numbers:
    if number > biggest:
        biggest = number
        print("biggest:", biggest)

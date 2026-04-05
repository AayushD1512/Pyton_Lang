count = 0

text = "This is a sample text. It contains several words, and we will count the number of vowels in it."

for c in text:
    if c.lower() in 'aeiou':
        count += 1

print("Number of vowels in the text:", count)

#check for palindrome by taking string input from user

s1 = input("Enter a string to check if it's a palindrome: ")

s2 = s1[::-1]
if s1 == s2:
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")

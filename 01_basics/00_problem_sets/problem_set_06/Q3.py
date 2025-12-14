# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams
comment = input("Enter the comment: ").lower()

spam_keywords = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

is_spam = False

for word in spam_keywords:
    if word in comment:
        is_spam = True
        break

if is_spam:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

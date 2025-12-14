# write a program to create a dictionary of hindi words with values as their english translation. Provide user with an option ro look it up!

dict={
    "nariyal":"coconut",
    "gareeb":"Poor",
    "ameer":"Rich",
    "bhagwan":"God",
    "namaste": "hello",
    "paani": "water",
    "ghar": "house",
    "kitaab": "book",
    "dost": "friend",
    "khana": "food",
    "shiksha": "education",
}

while True:
    word=input("Enter Hindi Word to Search: ").lower()

    if word=="exit":
        print("Thank you for using the dictionary! ")
        break
    if word in dict:
        print("English meaning: ", dict[word])
    else:
        print("Word not found in dictionary .")


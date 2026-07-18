books = {
    "Linux": "Available",
    "Maths": "Borrowed",
    "AI/ML": "Available",
    "Embedded Linux": "Available"
}

print("----------- Welcome to the Book Store -----------")
access=input("Press 'R' to read the book and 'S' to sell the book: ").lower()
if access=="R":
 for book in books:
    print(book)

 book = input("\nEnter the book required: ")

 if book not in books:
    print("Please enter a valid book name.")

 elif books[book] == "Available":
    print("The book is available. Go and grab it!")
    # books.update({"Linux":"Borrowed"})
    # print("The b")

 else:
    print("The book is currently borrowed.")

else:
   print("which book do you have")

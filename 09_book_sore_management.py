books = {
    "Linux": "Available",
    "Maths": "Borrowed",
    "AI/ML": "Available",
    "Embedded Linux": "Available"
}

while True:

    print("""
========== Library Management ==========
1. View Books
2. Borrow Book
3. Return Book
4. Sell Book
5. Search Book
6. Remove Book
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Books:")
        for book, status in books.items():
            print(f"{book:<20} {status}")

    elif choice == "2":
        book = input("Enter book name: ")

        if book not in books:
            print("Book not found.")

        elif books[book] == "Borrowed":
            print("Book is already borrowed.")

        else:
            books[book] = "Borrowed"
            print(f"{book} borrowed successfully.")

    elif choice == "3":
        book = input("Enter book name: ")

        if book not in books:
            print("Book not found.")

        elif books[book] == "Available":
            print("Book is already available.")

        else:
            books[book] = "Available"
            print(f"{book} returned successfully.")

    elif choice == "4":
        book = input("Enter book name: ")

        if book in books:
            print("Book already exists.")

        else:
            books[book] = "Available"
            print(f"{book} added successfully.")

    elif choice == "5":
        book = input("Enter book name: ")

        if book in books:
            print(f"{book} : {books[book]}")

        else:
            print("Book not found.")

    elif choice == "6":
        book = input("Enter book name: ")

        if book in books:
            del books[book]
            print(f"{book} removed successfully.")

        else:
            print("Book not found.")

    elif choice == "7":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")


#MY FIRST VERSION OF BOOK STORE MANAGEMENT SYSTEM


# print("----------- Welcome to the Book Store -----------")
# access=input("Press 'R' to read the book and 'S' to sell the book: ").lower()
# if access=="R":
#  for book in books:
#     print(book)

#  book = input("\nEnter the book required: ")

#  if book not in books:
#     print("Please enter a valid book name.")

#  elif books[book] == "Available":
#     print("The book is available. Go and grab it!")
#    #  books.update({"Linux":"Borrowed"})
#    #  print("The b")

#  else:
#     print("The book is currently borrowed.")

# else:
#    print("----------------SELL----------------")
#    book_info=input("Which book do you want to sell: ")
#    if book_info in books:
#       print("The book is already available in the store.")
#    else:
#       books[book_info] = "Available"
#       print(f"The book '{book_info}' has been added to the store.")
   
#    print("Current books in the store:")
#    for book,status in books.items():
#          print(f"{book}: {status}")
   
#    print("Thank you for selling the book. Have a great day!")

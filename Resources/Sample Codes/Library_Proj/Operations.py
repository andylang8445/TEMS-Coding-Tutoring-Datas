import FileIO as F
import time
import os
while True:
    os.system('cls' if os.name=='nt' else 'clear')
    print("Select from the menu:\n1. View Book List\n2. Ssearch Library\n3. Borrow from Library\n4. Return to Library\n5. Add new book to library\n6. Remove book from library\n7. End Software")
    choice = (input())
    if choice == '1':
        print("===== Printing List =====")
        f = F.read_DB()[0]
        if len(f) == 0:
            print("No Book Present!")
        for i in f:
            print(i[2]," - ",i[1]," By ",i[0])
        print("===== End Of List =====")
    elif choice == '2':
        print("Enter search options:\n1. author\n2. title\n3. code")
        choice2 = int(input())
        choice3 = input("Input search data: ")
        if choice2 == 1:
            f = F.search_DB("author",choice3)
        elif choice2 == 2:
            f = F.search_DB("title",choice3)
        elif choice2 == 3:
            f = F.search_DB("code",choice3)
        print("===== Printing Search Result =====")
        for i in f:
            print(i[2]," - ",i[1]," By ",i[0])
        print("===== End Of Result =====")
    elif choice == '3':
        code = input("Please enter the book code that you are borrowing: ")
        result = F.borrow_from(code)
        if result == 2:
            print("The book have been successfully borrowed the book",code," from the library")
        elif result == 1:
            print("Please check the code!\nThe code inputted does not exist in the library database")
        elif result == 0:
            print("Please check the code!\nThe code you entered is already borrowed")
        else:
            print("ERROR!")
    elif choice == '4':
        code = input("Please enter the book code that you are returning: ")
        result = F.return_to(code)
        if result == 1:
            print("Sucessfully returned the book with code ",code)
        elif result == 2:
            print("The book was not borrowed from the library!\nPlease see the librarian")
        elif result == 0:
            print("The book ",code,"does not exist in the library database!\nDouble check the code")
        else:
            print("ERROR!")
    elif choice =='5':
        print("===== Adding new book =====")
        auth = input("Please enter the author of the book: ")
        title = input("Please enter the title of the book: ")
        code = input("Please enter the code of the book: ")
        result = F.new_Book(auth, title, code)
        if result == True:
            print("Successfully added the book", code, "to the library database")
        else:
            print("Error!\nThere is already registered book with the code!")
        print("===== End of Adding =====")
    elif choice == '6':
        print("===== Remove existing book =====")
        code = input("Please input the code of the book that you are trying to remove: ")
        result = F.remove_Book(code)
        if result == True:
            print("Book", code,"have been successfully removed")
        else:
            print("Failed to remove!\nCheck if the book is borrowed from the library\nIf not, double check the code")
        print("===== End of Remove =====")
    elif choice == '7':
        print("End of Library Management Software\nCreated by Andy Yun")
        break
    else:
        print("Wrong choice!")
    time.sleep(2.5)
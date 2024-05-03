from datetime import datetime, timedelta
#Creating the class library
class Library:
    def __init__(self):
        self.books = {}
        self.rented_books={}#To Track the books records in the bookshelf
    #Creating a function to add books to the bookshelf
    def addbook(self, title, author, isbn):
        if isbn not in self.books:
            self.books[isbn]={"title": title, "author": author}
            print("Book added to the bookshelf.")
        else:
            print("Book already present in the bookshelf, so no need to add more.")
    #Creating a function to remove a given book from the bookshelf
    def removebook(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} removed from the bookshelf.")
        else:
            print("Book not found in the bookshelf.")
    #Creating a function to search for a book in the bookshelf
    def searchbook(self, query):
        found_books=[]
        for isbn, book_info in self.books.items():
            if (query.lower() in book_info['title'].lower() or
                    query.lower() in book_info['author'].lower() or
                    query.lower() in isbn.lower()):
                found_books.append((isbn, book_info))
        return found_books
    #Creating a function to display all the books in the bookshelf
    def displaybooks(self):
        if self.books:
            print("Books in the bookshelf:")
            for isbn, book_info in self.books.items():
                print(f"ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}")
        else:
            print("No books found in the bookshelf.")
    #Creating a function to gift a book to a friend so rent is calculated in this case
    def giftbook(self, isbn):
        if isbn in self.books:
            book_info = self.books.pop(isbn)
            print(f"Book '{book_info['title']}' has been gifted to a friend.")
        else:
            print("Book not found in the bookshelf.")
    #Creating a function to rent a book to a random person
    def rentbook(self, isbn, name, address, phone, days):
        rent_per_day=30#Rent oer day is 30 rupees 
        if isbn in self.books:
            #To calculate the total rent of the book and where the book is and the book informartion
            total_rent=rent_per_day * days
            date_of_issue = datetime.now()  # Current date and time as date of issue
            due_date = date_of_issue + timedelta(days=days)
            #Giving the rental information
            rental_info={
                "title": self.books[isbn]["title"],
                "name": name,
                "address": address,
                "phone": phone,
                "days": days,
                "rent": total_rent,
                "date_of_issue": date_of_issue,
                "due_date": due_date
            }
            #To store the rental information in the given library
            self.rented_books[isbn] = rental_info

            print(f"Book '{self.books[isbn]['title']}' has been rented out to {name} for {days} days.")
            print(f"Total rent to be paid: {total_rent} rupees.")
            print(f"Due date: {due_date.strftime('%Y-%m-%d')}")
        else:
            print("Book not found in the bookshelf.")

    #Creating a function to calculate fine for late return
    def calculatefine(self, isbn, date_of_return):
        if isbn in self.rented_books:
            rental_info = self.rented_books[isbn]
            due_date = rental_info["due_date"]
            late_days = (date_of_return - due_date).days
            
            if late_days > 0:
                fine_per_day = 20  # Fine is 20 rupees per day
                fine = fine_per_day * late_days
                print(f"Fine for {late_days} late days: {fine} rupees.")
            else:
                print("No fine. The book was returned on time.")
        else:
            print("Book not found in the rented books list.")

    #Creating a function to return a rented book
    def return_book(self, isbn, date_of_return):
        if isbn in self.rented_books:
            #Calculating the fine for the late return
            self.calculate_fine(isbn, date_of_return)
            
            #Removing the book from rented books
            rental_info = self.rented_books.pop(isbn)
            
            #Adding the book back to the library's bookshelf
            self.books[isbn] = {"title": rental_info["title"], "author": rental_info.get("author", "Unknown")}
            
            print(f"Book '{rental_info['title']}' has been returned.")
        else:
            print("Book not found in the rented books list.")
#Creating the main function
def main():
    library = Library()
    #F=GIving choice to the user
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Gift Book")
        print("6. Rent Book")
        print("7. Return Book")
        print("8. Exit")
        #Asking user for the choice
        choice = input("Enter your choice: ")
        #Giving choices to the user
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.addbook(title, author, isbn)
        elif choice == "2":
            isbn = input("Enter the ISBN of the book to remove: ")
            library.removebook(isbn)
        elif choice == "3":
            query = input("Enter details of the book to search: ")
            found_books = library.searchbook(query)
            if found_books:
                print("Books found:")
                for isbn, book_info in found_books:
                    print(f"ISBN: {isbn}, Title: {book_info['title']}, Author: {book_info['author']}")
            else:
                print("No books found.")
        elif choice == "4":
            library.displaybooks()
        elif choice == "5":
            isbn = input("Enter the ISBN of the book to gift: ")
            library.giftbook(isbn)
        elif choice == "6":
            isbn = input("Enter the ISBN of the book to rent: ")
            name = input("Enter the name of the person renting the book: ")
            address = input("Enter the address of the person: ")
            phone = input("Enter the phone number of the person: ")
            days = int(input("Enter the number of days to rent the book: "))
            library.rentbook(isbn, name, address, phone, days)
        elif choice == "7":
            isbn = input("Enter the ISBN of the book to return: ")
            date_of_return = input("Enter the date of return (YYYY-MM-DD): ")
            date_of_return = datetime.strptime(date_of_return, '%Y-%m-%d')
            library.returnbook(isbn, date_of_return)
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
#Calling of the main function
if __name__ == "__main__":
    main()
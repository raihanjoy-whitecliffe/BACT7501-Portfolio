class Book:
    def __init__(self, book_title, book_author, copies_available):
        self.book_title = book_title
        self.book_author = book_author
        self.copies_available = copies_available
    def display_book(self) :
        print(self.book_title)
        print(self.book_author)
        print(self.copies_available)
    def borrow_book(self) :
        if self.copies_available > 0:
           self.copies_available -= 1
           print("Book Borrowed Successfully")
        else:
            print("No Copies Available")
    def return_book(self) :
        self.copies_available+=1
        print("Book Returned Successfully")
book1= Book("Harry Potter and the Chamber of Secrets","J.K Rowling",11)
book1.display_book()
book1.borrow_book()
book1.display_book()
book1.return_book()
book1.display_book()
book2= Book("Harry Potter and the Prisoner of Azkaban","J.K Rowling",43)
book2.display_book()
book2.borrow_book()
book2.display_book()
book2.return_book()
book2.display_book()
book3= Book("The Hunger Games","Suzanne Collins",9)
book3.display_book()
book3.borrow_book()
book3.display_book()
book3.return_book()
book3.display_book()
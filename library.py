class Book:

    def __init__(self, title, author, price, availability=True):

        self.title = title
        self.author = author
        self.price = price
        self.availability = availability

    def display_info(self):
        print("Name is ", self.title)
        print("Author is ", self.author)
        print("Price is ", self.price)
        print("status", self.availability)

    def borrow_book(self):
        if self.availability:
            print("book is available")
            self.availability = False
        else:
            print("already borrowed")

    # def mark_avalable(self):
    #     self.availability = True


book1 = Book("hh","yy",4)
book1.display_info()
book1.borrow_book()

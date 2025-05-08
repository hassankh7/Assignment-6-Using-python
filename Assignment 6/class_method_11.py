

class Book:
    # Class variable to keep count of total books
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Increment total_books count whenever a book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print(f"Total books added: {cls.total_books}")


# Create some book objects
book1 = Book("Python Programming")
book2 = Book("Data Science Essentials")
book3 = Book("Machine Learning Guide")

# Display total books added
Book.show_total_books()

class Library:
    def __init__(self):
        self.books_title = []
        title = 0

    def add_book(self, title):
        self.books_title.append(title)

    def show_book(self):
        print("\nTitle of books\n")

        for book in self.books_title:
            print(book.title())


def main():
    library = Library()
    library.add_book("Atomic Habit")
    library.add_book("Alchemist")
    library.add_book("Moon shot")
    library.add_book("Thing and grow big")
    library.add_book("Grit")

    library.show_book()

if __name__ == "__main__":
    main()

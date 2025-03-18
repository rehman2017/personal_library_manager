import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, year, genre, read_status):
        book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read_status": bool(read_status)
        }
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                status = "Read" if book['read_status'] else "Unread"
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Status: {status}")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower()]
        if results:
            for book in results:
                status = "Read" if book['read_status'] else "Unread"
                print(f"{book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']}, Status: {status}")
        else:
            print("No matching books found.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"Book '{title}' removed successfully!")
                return
        print("Book not found.")

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book["read_status"])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books: {total_books}")
        print(f"Read books: {read_books} ({percentage_read:.2f}%)")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            genre = input("Enter book genre: ")
            read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
            manager.add_book(title, author, year, genre, read_status)
        elif choice == "2":
            title = input("Enter the book title to remove: ")
            manager.remove_book(title)
        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            manager.search_book(keyword)
        elif choice == "4":
            manager.view_books()
        elif choice == "5":
            manager.display_statistics()
        elif choice == "6":
            print("Exiting the library manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

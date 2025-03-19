from collections import Counter, defaultdict, deque, namedtuple
from collections import OrderedDict

# Book Details - namedtuple
Book = namedtuple('Book', ['book_id', 'title', 'author'])

# Initialize data structures
book_inventory = Counter()  # To track book copies
borrow_history = defaultdict(deque)  # To track borrowing history per user
new_arrivals = OrderedDict()  # To track new arrivals
borrow_requests_vip = deque()  # To prioritize VIP member borrow requests
borrow_count = Counter()  # To track borrow frequency of books

# Add a new book to the inventory
def add_book(book, count):
    book_inventory[book.title] += count
    new_arrivals[book.title] = book  # Add to new arrivals
    print(f"Added {count} copies of '{book.title}' by {book.author}.")

# Issue a book to a user
def issue_book(user_id, book_title, is_vip=False):
    if is_vip:
        borrow_requests_vip.append((user_id, book_title))
        print(f"VIP request added for '{book_title}' by User {user_id}.")
        return

    if book_inventory[book_title] > 0:
        book_inventory[book_title] -= 1
        borrow_count[book_title] += 1
        borrow_history[user_id].appendleft(book_title)  # Add to borrowing history
        if len(borrow_history[user_id]) > 3:
            borrow_history[user_id].pop()  # Remove oldest entry if more than 3
        print(f"Book '{book_title}' issued to User {user_id}.")
    else:
        print(f"Sorry, '{book_title}' is not available.")

# Return a book to the inventory
def return_book(book_title):
    book_inventory[book_title] += 1
    print(f"Book '{book_title}' returned successfully.")

# Process VIP borrow requests
def process_vip_requests():
    while borrow_requests_vip:
        user_id, book_title = borrow_requests_vip.popleft()
        issue_book(user_id, book_title)

# Display new arrivals
def display_new_arrivals():
    print("\nNew Arrivals in the Library:")
    for book in new_arrivals.values():
        print(f"{book.title} by {book.author} (ID: {book.book_id})")

# Display borrowing history for a user
def display_borrow_history(user_id):
    print(f"\nBorrowing History for User {user_id}:")
    if user_id in borrow_history:
        for book in borrow_history[user_id]:
            print(book)
    else:
        print("No borrowing history found.")

# Print the top 2 most borrowed books
def top_borrowed_books():
    print("\nTop 2 Most Borrowed Books:")
    for book, count in borrow_count.most_common(2):
        print(f"{book}: borrowed {count} times")

# Example usage
if _name_ == "_main_":
    # Adding books
    book1 = Book(1, "Ikigai", "Garcia")
    book2 = Book(2, "2022", "Hanseo")
    book3 = Book(3, "Lost Dragon", "Kimchi")

    add_book(book1, 5)
    add_book(book2, 3)
    add_book(book3, 4)

    # Borrowing books
    issue_book("User1", "Ikigai")
    issue_book("User1", "2022")
    issue_book("User2", "Lost Dragon")
    issue_book("User3", "Ikigai")
    issue_book("VIP1", "2022", is_vip=True)

    # Process VIP requests
    process_vip_requests()

    # Returning a book
    return_book("2022")

    # Display information
    top_borrowed_books()
    display_borrow_history("User1")
    display_new_arrivals()
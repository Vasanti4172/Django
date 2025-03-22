from collections import Counter, defaultdict, deque 
from collections import OrderedDict, namedtuple

Book = namedtuple('Book', ['book_id', 'title', 'author'])

book_inventory = Counter()
borrow_history = defaultdict(deque)

new_arrivals =OrderedDict()

borrow_requests_vip = deque()

borrow_count=Counter()

def add_book(book, count):

    book_inventory[book.title] += count

    new_arrivals[book.title] = book

def issue_book(user_id, book_title, is_vip=False):

    if is_vip:

        borrow_requests_vip.append((user_id, book_title))

        return

    if book_inventory[book_title] > 0:

        book_inventory[book_title] = 1

        borrow_count[book_title] += 1

        borrow_history[user_id].appendleft(book_title)

    if len(borrow_history[user_id]) > 3:

        borrow_history[user_id].pop()

def return_book(book_title):
    book_inventory[book_title] +1

def process_vip_requests():

    while borrow_requests_vip:

        user_id, book_title = borrow_requests_vip.popleft()

        issue_book(user_id, book_title)

def display_new_arrivals():

    print("\nNew Arrivals in the Library:")

    for book in new_arrivals.values():

        print(f"{book.title} by (book.author) (ID: {book.book_id})")

def display_borrow_history(user_id):

    print(f"\nBorrowing History for User (user_id):")

    if user_id in borrow_history:

        for book in borrow_history[user_id]:

            print(book)

    else:

        print("No borrowing history found.")

def top_borrowed_books():

    print("\nTop 2 Most Borrowed Books:")
    for book, count in borrow_count.most_common(2):

        print(f" {book}: borrowed {count} times")

if __name__ == "__main__":

    book1 =Book(1, "Ikigai", "Garcia")

    book2= Book(2, "2022", "Hanseo")

    book3 =Book(3, "Lost Dragon", "Kimchi")

    add_book(book1, 5)

    add_book(book2, 3)

    add_book(book3, 4)

    issue_book("User1", "Ikigai")

    issue_book("User1", "2022")

    issue_book("User2", "Lost Dragon")

    issue_book("User3", "Ikigai")

    issue_book("VIP1", "2022", is_vip=True)

    process_vip_requests()

    return_book("2022")

    top_borrowed_books()
    display_borrow_history("User1")

    display_new_arrivals()
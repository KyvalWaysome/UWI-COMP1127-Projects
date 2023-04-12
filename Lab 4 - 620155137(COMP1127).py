def makebook(isbn,title,authors,genre,year,qtystck,saleprice):
 """constructor - creates a book"""
 return [isbn,title,authors,genre,year,qtystck,saleprice]
def bookshop():
 """constructor- creates a new bookshop"""
 return ("bookshop",[])
def add_book(book,bookshop):
 """constructor - adds a book to the bookshop"""
 return bookshop[1].append(book)
def get_isbn(book):
    
  return book[0]
def get_title(book):
    
 return book[1]
def get_authors(book):
    
 return book[2]
def get_genre(book):
   
 return book[3]
def get_year(book):
   
 return book[4]
def get_qty(book):
   
 return book[5]
def get_saleprice(book):
    
 return book[6]


def co_authors(book):

 if len(get_authors(book)) > 1:#len checks for multiple authors
    return get_authors(book)[1:] #list of co authors
 else:
        return[]#if it is single authored

def check_price(bookshop, isbn):
    for book in books(bookshop):#take on the value of each book in the list of books
        if isbn == get_isbn(book):#checking the isbn you're trying to find
            return get_saleprice(book)#corresponding sale price of the book
    return "Book not found" #if the isbn doesnt exist
        
def books_to_reorder(bookshop, reorder):#bookshop and integer
    book_order = [(get_isbn(book), get_title(book)) for book in books(bookshop) if get_qty(book) <= reorder]
    return book_order #the books whose quantities are below or equal to reorder are returned in a tuple           
    

# Student library program 
# library --> contains books with status (available/issued) ✅✅
# options --> issue a new book / return existing book 


#book1 : available/issued
#book2 : available/issued

#int / float
#str / char
#bool
#list []/ tuple ()
#dict {:}/ set {}

from pprint import pprint

library = dict()
library['indian history'] 					= 'available'
library['political science'] 				= 'available'
library['vedic maths'] 						= 'available'
library['ocean science'] 					= 'available'
library['space exploration'] 				= 'available'
library['geography of indian subcontinent'] = 'available'

pprint(library)

# student gets book issued to them
def issue_book(book_name):
	library[book_name] = 'issued'

# student returns the book back to library
def return_book(book_name):
	library[book_name] = 'available'

def visit_library():
	option = input("(1) to issue a new book or (2) return an existing one ?")

	if option == '1':
		book1 = input("which book you would like to get?")
		book1 = book1.strip()
		issue_book(book1)
	
	if option == '2':
		book2 = input("which book you would like to return?")
		book2 = book2.strip()
		return_book(book2)

	pprint(library) 


visit_library()




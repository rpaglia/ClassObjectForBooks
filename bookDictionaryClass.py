# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:09:38 2021
@author: Richard Paglia

Book Class
"""

totalDict = {}
allBooks = []

class bookClass(object):
    def __init__(self, totalDict, allBooks):
        self._totalDict = totalDict
        self._allBooks = allBooks
      
    def bookDeletion():
        #If 2 books same name, which to delete, currently older book removed..
            bookToDelete = input('Book to delete: ')
            for element in allBooks:
                if bookToDelete in element['Name']:
                    result = next(item for item in allBooks if item['Name'] == bookToDelete)
                    allBooks.remove(result)
                    print(f'\033[0;43;mDeleting the book "{bookToDelete}" from the dictionary!!\n\033[0;0;m')
                    return
            
            print(f'\033[0;31;m{bookToDelete} does not exists in dictionary.\033[0;0;m')
    
    def bookAddition():
        #Need to add error correction to this block!!
        bookName = input('Enter name of book: ')
        bookAuthor = input('Enter name of the author: ')
        bookLength = int(input('Enter number of pages: '))
        bookGenre = input('Enter genre of the book: ')
        bookYear = int(input('Enter the year the book was written: '))
        bookSet = input('Is book part of a set(y/n): ').lower()
        bookInfo={'Name':bookName,'Author':bookAuthor,'Pages':bookLength,'Genre':bookGenre, 'Year Written':bookYear, 'Bookset': bookSet}
        totalDict = bookInfo
        allBooks.append(totalDict)
        return allBooks 
     
    def menu(allBooks):
        while True:
            print ("\n\n\nBook Dictionary Menu")
            print ("\033[0;36;m----------------------\033[0;0;m")
            print ("1) Display Book Dictionary")
            print ("2) Add Book to Dictionary")
            print ("3) Remove Book from Dictionary")    
            print ("Q) Exit\n")
            choice = input('Enter your choice: ').lower()
            
            if choice == '1':
                if allBooks:
                    allBooksSorted = sorted(allBooks , key = lambda i: (i['Name'], i['Author']))
                    print('\n\nCurrent Book Dictionary')
                    print("\033[0;36;m-------------------------\033[0;0;m")
                    print(*allBooksSorted, sep = '\n' )
                else:
                    print("\n\033[0;31;mThe book dictionary is currently empty...\033[0;0;m")
                    input('Press Enter to return to menu...')
            elif choice == '2':
                bookClass.bookAddition()
            elif choice == '3':
                bookClass.bookDeletion()
            elif choice == 'q':
                return
            else:
                print(f'\033[0;31;mNot a correct choice: <{choice}>,try again\033[0;0;m')
 
if __name__ == '__main__':
    book1 = bookClass(totalDict, allBooks)
    book1.allBooks = []
    bookClass.menu(allBooks)    




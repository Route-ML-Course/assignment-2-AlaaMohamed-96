class library :
    def __init__(self,Title,Authors,num_copies_avalb,num_copies_borrowed,Loan_period):
        self.title = Title
        self.authors = Authors
        self.num_copies_avali = num_copies_avalb
        self.num_copies_borowed = num_copies_borrowed
        self.loan_period = Loan_period

    def get_title(self):
        return self.title
    def set_title(self,value):
        self.title=value
    def get_autors(self):
        return self.authors
    def set_autors(self, value):
        self.authors = value
    def get_num_copies_avali(self):
        return self.num_copies_avali
    def set_num_copies_avali(self,value):
        self.num_copies_avali=value
    def get_num_copies_borowed(self):
        return self.num_copies_borowed
    def set_num_copies_borowed(self,value):
        self.num_copies_borowed=value
    def get_loan_period(self):
        return self.loan_period
    def set_loan_period(self,value):
        self.loan_period=value
    def __repr__(self):
        return f"library([{self.title},{self.num_copies_avali},{self.authors},{self.num_copies_borowed},{self.loan_period})"

class uesr :
    def __init__(self,Name,Id,book_Borrowed,Email,user_level):
        self.name = Name
        self.id = Id
        self.book_borrowed = book_Borrowed
        self.email = Email
        self.user_level = user_level


    def get_name(self):
        return self.name
    def set_name(self,value):
        self.name=value

    def get_id(self):
        return self.id
    def set_id(self,value):
        self.id=value

    def get_book_borrowed(self):
        return self.book_borrowed
    def set_book_borrowed(self,value):
        self.book_borrowed=value

    def get_email(self):
        return self.email
    def set_email(self,value):
        self.email=value

    def get_user_level(self):
        return self.user_level
    def set_user_level(self,value):
        self.user_level=value

class Mainlibrary :
    def __init__(self,user_level):
        self.user_level = user_level
        self.List_bookes =  []
        self.List_bookes_Borrow = []
    def get_user_level(self):
        return self.user_level
    def set_user_level(self,value):
        self.user_level= value
    def get_book(self):
        return self.List_bookes
    def set_book(self,value):
        self.List_bookes.append(value)

    def Borrow_book(self,book_title):
        for i in self.List_bookes:
            if book_title == i.get_title() :
                self.List_bookes_Borrow.append(i)
                self.List_bookes.pop(i)
            else:
                return "the book not found"
    def Return_book (self,book):
        self.List_bookes.append(book)
    def Search_book(self,book_title):
        for i in self.List_bookes:
            if book_title == i.get_title():
                return "book is found"
            else:
                return "book not found"
    def Extend_period_Book(self,time,Book_title):
        for i in self.List_bookes:
            if Book_title == i.get_title():
                i.set_loan_period(time)
            else:
                return "the book not found"
    def Remove_Book(self,Book_Title):
        for i in self.List_bookes:
            if Book_Title == i.get_title() :
                self.List_bookes.pop(i)
                return "book is removed"
            else:
                return "the book not found"

userLevel = input(" If librarian enter 1 , If user enter 2 ")
if userLevel == "1":
    UserName = input("enter your name")
    UserId = input("enter your id")
    UserEmail = input("enter your email")
    user1 = uesr(UserName, UserId, "", UserEmail, userLevel)
    book1 = library("comedy","sss",3,1,20)
    book2 = library("action","aaa",1,0,20)
    mainSystem = Mainlibrary(userLevel)
    mainSystem.set_book(book1)
    mainSystem.set_book(book2)
    UserChoose = input("Add a book to the system enter 1"
                       "Remove a book from the system enter 2"
                       "Search for books enter 3")
    if UserChoose == "1":
        bookTitle = input("enter book title")
        bookAuthors = input("enter book Authors")
        num_copies_avalb = input("enter Number of copies available at library")
        num_copies_borrowed = input("enter Number of copies borrowed")
        Loan_period = input("enter lone period ")
        book= library(bookTitle,bookAuthors,num_copies_avalb,num_copies_borrowed,Loan_period)
        mainSystem.set_book(book)
    if UserChoose == "2":
        book_title = input(" enter book title")
        print(mainSystem.Remove_Book(book_title))
    if UserChoose == "3":
        book_title = input(" enter book title")
        print(mainSystem.Search_book(book_title))
if userLevel == "2" :
    UserName = input("enter your name")
    UserId = input("enter your id")
    UserEmail = input("enter your email")
    user1 = uesr(UserName,UserId,"",UserEmail,userLevel)
    mainSystem = Mainlibrary(userLevel)
    UserChose = input("Borrow a book enter 1"
                      " Return a book enter 2"
                      "Search for a book enter 3"
                      "Extend loan period for a borrowed book enter 4")
    if UserChose == "1":
        bookTitle = input("enter book title")
        mainSystem.Borrow_book(bookTitle)
    if UserChose == "2":
        pass
    if UserChose == "3":
        bookTitle = input("enter book title")
        mainSystem.Search_book(bookTitle)
    if UserChose == "4":
        bookTitle = input("enter book title")
        time = input("enter period time")
        mainSystem.Extend_period_Book(time,bookTitle)
    else:
        print("error choose")





# user1 = uesr("ahmed",1111,"","aaaaa@mail",1)
# book1 = library("comedy","sss",3,1,20)
# book2 = library("action","aaa",1,0,20)
# book3= library("action","aaa",1,0,20)
# main_system = Mainlibrary(user1.get_user_level())
# main_system.set_book(book1)
# main_system.set_book(book2)
# # print(main_system.Search_book("comedy"))
# # print(main_system.Search_book("aaaa"))
# # main_system.Borrow_book("comedy")
# main_system.Extend_period_Book(600,"comedy")
# print(main_system.List_bookes)







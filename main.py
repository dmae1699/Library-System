class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False
        
    def borrow(self):
        if self.is_borrowed:
            print(f"{self.title}already borrowed.")
        else:
            print(f"{self.title} has been borrowed.")
            self.is_borrowed=True 
    
    def return_book(self):
        if not self.is_borrowed:
            print(f"{self.title} is not borrowed.")
        else:
            print(f"{self.title} has been returned.")
            self.is_borrowed=False
    
    def __str__(self):
        if not self.is_borrowed:
            status="available"
        else:
            status="borrowed"
        return f"{self.title} information:\nTitle: {self.title}\nAuthor: {self.author}\nStatus of {self.title}: {status}"
        
b=Book("Wishing Chair","Enid Blyton")
b1=Book("Harry Potter and The Deathly Hallows","JK Rowling")
b2=Book("Cloudburst","Wilbur Smith")
print("=" * 28)
print("LIBRARY SYSTEM".center(28))
print("=" * 28)
print(f"{b.title} by {b.author}\n{b1.title} by {b1.author}\n{b2.title} by {b2.author}\n")
b.borrow()
b1.borrow()
b2.borrow()
b.return_book()
print()
print((b))
print()
print(b1)
print()
print(b2)

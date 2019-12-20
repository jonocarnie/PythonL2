class Book():
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Title: {self.title},\nAuthor: {self.author}"

    # def __str__(self):
    #     return f"Title: {self.title}\nAuthor: {self.author}"
    def __len__(self):
        return self.pages
    
mybook = Book("Python rocks!", 'Jonathan', 250)


print(mybook)
length = len(mybook)

print (f"Length of book: {length} pages.")
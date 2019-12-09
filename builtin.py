class Book():
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        
        return f"Title: {self.title},\nAuthor: {self.author}"

    
mybook = Book("Python rocks!", 'Jonathan', 250)

print(mybook)
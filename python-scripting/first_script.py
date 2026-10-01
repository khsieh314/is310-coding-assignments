
favorite_books = [
    {
        "title": "The Very Hungry Caterpillar",
        "release_year": 1969,
        "author": "Eric Carle"
    },
    {
        "title" : "Where the Sidewalk Ends",
        "release_year" : 1974,
        "author" : "Shel Silverstein"
    },
    {
        "title" : "This is Not My Hat",
        "release_year" : 2012,
        "author" : "Jon Klassen"
    },
    {
        "title": "Zen Shorts",
        "release_year": 2005,
        "author": "Jon J. Muth"
    },
    {
        "title": "The Dot",
        "release_year": 2003,
        "author": "Peter H. Reynolds"
    },
]

# print(favorite_books)

# for book in favorite_books:
#    print(book["title"])

def book_release_year(book):
    if book["release_year"] < 2000:
        return ("This book was released before 2000")
    else:
        return (book["title"])

#print(book_release_year(favorite_books[0]))

recent_books = []

for book in favorite_books:
    year = book_release_year(book)
    if year != ("This book was released before 2000"):
        recent_books.append(year)


print(recent_books)

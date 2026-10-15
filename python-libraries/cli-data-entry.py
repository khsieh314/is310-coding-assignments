import json
from pathlib import Path
output_file = Path("favorite_childhood_books.json")

from rich.console import Console
console = Console()
from rich.table import Table

#console.print("Testing text", style="dark_green")

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

console.print("Here's the inital data of the Favorite Childhood Books Table", style="dark_green")

def initial_table(book_list):
    table = Table(title="Favorite Childhood Books", style="dark_green")
    table.add_column("Title", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Release Year", justify="center")
    """ table.add_row("The Very Hungry Caterpillar", "Eric Carle", "1968")
    table.add_row("Where the Sidewalk Ends", "Shel Silverstein", "1974")
    table.add_row("This is Not My Hat", "Jon Klassen", "2012")
    table.add_row("Zen Shorts", "Jon J. Muth", "2005")
    table.add_row("The Dot", "Peter H. Reynolds", "2003") """
    for book in book_list:
        table.add_row(book["title"], book["author"], str(book["release_year"]))
    
    console.print(table)

initial_table(favorite_books)

console.print("Let's add your favorite book to our table", style="dark_green")

def add_book():
    title = console.input("Title: ")
    author = console.input("Author: ")
    year_published = console.input("Release Year: ")

    new_book = {
        "title": title,
        "author": author,
        "release_year": int(year_published)
    }

    return new_book


enter_book = console.input("Would you like to add a book to the table? (y/n): ")
multiple_entries = True

if enter_book == "y" or enter_book == "Y" or enter_book == "Yes" or enter_book == "yes":
    while multiple_entries == True:
        new_entry = add_book()
        is_correct = console.input("Is this information correct? (y/n): ")
        if is_correct == "y" or is_correct == "Y" or is_correct == "Yes" or is_correct == "yes":
            favorite_books.append(new_entry)
            another_one = console.input("Do you want to add another book? (y/n): ")
            if another_one == "n" or another_one == "N" or another_one == "No" or another_one == "no":
                multiple_entries = False
            elif another_one == "y" or another_one == "Y" or another_one == "Yes" or another_one == "yes":
                console.print("Begin adding your next entry")
            else:
                console.print("This command is not recognized, ending input")
                multiple_entries = False



#console.print(favorite_books)
initial_table(favorite_books)

output_file.write_text(json.dumps(favorite_books, indent=4), encoding="utf-8")

console.print("Your data has been saved!")
console.print(f"File saved in {output_file.resolve()}")
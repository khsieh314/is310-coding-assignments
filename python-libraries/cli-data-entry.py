"""import json
from pathlib import Path
output_file = Path("favorite_childhood_books.json")"""

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

def initial_table():
    table = Table(title="Favorite Childhood Books", style="dark_green")
    table.add_column("Title", justify="center")
    table.add_column("Author", justify="center")
    table.add_column("Year Published", justify="center")
    table.add_row("The Very Hungry Caterpillar", "Eric Carle", "1968")
    table.add_row("Where the Sidewalk Ends", "Shel Silverstein", "1974")
    table.add_row("This is Not My Hat", "Jon Klassen", "2012")
    table.add_row("Zen Shorts", "Jon J. Muth", "2005")
    table.add_row("The Dot", "Peter H. Reynolds", "2003")
    
    return(table)

console.print(initial_table())

console.print("Let's add your favorite book to our table", style="dark_green")

def add_book():
    title = console.input("Title: ")
    author = console.input("Author: ")
    year_published = console.input("Year Published: ")

    new_book = {
        "title": title,
        "author": author,
        "release_year": int(year_published)
    }

    return new_book




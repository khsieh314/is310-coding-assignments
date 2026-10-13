from rich.console import Console
console = Console()
from rich.table import Table

#console.print("Testing text", style="dark_green")

table = Table(title="Favorite Childhood Books", style="dark_green")
table.add_column("Title", justify="center")
table.add_column("Author", justify="center")
table.add_column("Year Published", justify="center")
table.add_row("The Very Hungry Caterpillar", "Eric Carle", "1968")
table.add_row("Where the Sidewalk Ends", "Shel Silverstein", "1974")
table.add_row("This is Not My Hat", "Jon Klassen", "2012")
table.add_row("Zen Shorts", "Jon J. Muth", "2005")
table.add_row("The Dot", "Peter H. Reynolds", "2003")

console.print(table)
# This is a sample set of rich as data formatter
#   https://www.freecodecamp.org/news/use-the-rich-library-in-python/
#   https://rich.readthedocs.io/en/stable/reference/text.html

from rich import print as rprint


# 1 Datatypes diff.
nums_list = [1, 2, 3, 4]
rprint(nums_list)

nums_tuple = (1, 2, 3, 4)
rprint(nums_tuple)

nums_dict = {'nums_list': nums_list, 'nums_tuple': nums_tuple}
rprint(nums_dict)

bool_list = [True, False]
rprint(bool_list)

str = "Hello world! :banana:"
rprint(str)

str = "Hello [red]world![/red]"
rprint(str)



# 2 Inspect feature
from rich import inspect
import rich

inspect(rich)



# 3 Terminal formatting
from rich.console import Console

console = Console()

def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two # here | means concat or merge values based upon type (here, dict1 and dict2)
    console.log(merged_dict, log_locals=True)

merge_dict({'id': 1}, {'name': 'Ashutosh'})



# 4 Tree format for hierarchical data such as File Systems
from rich.tree import Tree
from rich import print as rprint

tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("Brother").add("Girlfriend").add("Girlfriend's daughter")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)



# 5 Progress bars
# a.-
from rich.progress import track
from time import sleep

def process_data():
    sleep(0.3)
for _ in track(range(10), description=f'[green]Processing data:'):
    process_data()

# b.- multi progress bars
import time
from rich.progress import Progress

with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...", total=100)
    task2 = progress.add_task("[green]Processing...", total=100)
    task3 = progress.add_task("[cyan]Installing...", total=100)

    while not progress.finished:
        progress.update(task1, advance=0.9)
        progress.update(task2, advance=0.6)
        progress.update(task3, advance=0.3)
        time.sleep(0.02)
        


# 6 Console (animated icon as last line)
from rich.console import Console
from time import sleep

console = Console()

data = [1, 2, 3, 4, 5]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish fetching data[/green] {num}")

    console.log(f'[bold][red]Done!')



# 7 Console (Buttons/Panels)
import json
from urllib.request import urlopen
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

def get_content(user):
    """Extract text from user dict."""
    country = user["location"]["country"]
    name = f"{user['name']['first']} {user['name']['last']}"
    return f"[b]{name}[/b]\n[yellow]{country}"

console = Console()
users = json.loads(urlopen("https://randomuser.me/api/?results=30").read())["results"]
user_renderables = [Panel(get_content(user), expand=True) for user in users]
console.print(Columns(user_renderables))



# 8 Tables
from rich.console import Console
from rich.table import Table

table = Table(title="Todo List")

table.add_column("S. No.", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta")
table.add_column("Status", justify="right", style="green")

table.add_row("1", "Buy Milk", "✅")
table.add_row("2", "Buy Bread", "✅")
table.add_row("3", "Buy Jam", "❌")

console = Console()
console.print(table)



# 9 More tables
from rich.table import Table  
from rich.console import Console  
console = Console()  
table = Table(title="My Table", style="green", header_style="bold white")  
table.add_column("Name", style="cyan", justify="right")  
table.add_column("Age", style="magenta", justify="center")  
table.add_row("Alice", "25", style="bold")  
table.add_row("Bob", "32")  
console.print(table) 



# 10 Logging with rich
import logging  
from rich.logging import RichHandler  
logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  
handler = RichHandler(show_path=False)  
handler.setFormatter(logging.Formatter("%(message)s"))  
logger.addHandler(handler)  
logger.info("This is an info message")  
logger.warning("This is a warning message")  
logger.error("This is an error message")  



# 10 Syntax highlight
from rich.console import Console  
from rich.syntax import Syntax  
console = Console()  
code = """ 
def my_function(): 
    print("Hello, world!") 
"""  
console.print(Syntax(code, "python", theme="monokai", line_numbers=True))  



# 11 Text wrapping (align and wrap)
from rich.align import Align
from rich.console import Console
console = Console()
text = "Mar 14, 2023 — Learn how to use Elasticsearch in Python. \nStep 1. Install Elasticsearch \nStep 2.Install the Elasticsearch Python Client \n...."
console.print(Align.center(text, width=20, vertical="middle", style="on red", height=console.height))
console.print(Align.center(text, width=20, vertical="bottom", style="on black", height=console.height, pad=True))


from rich.text import Text
from rich.console import Console
console = Console()
text = "Mar 14, 2023 — Learn how to use Elasticsearch in Python. \nStep 1. Install Elasticsearch \nStep 2.Install the Elasticsearch Python Client \n...."
console.print(text, sep="_", end='\n', width=20, emoji=True, style=None, justify="full", no_wrap=False, new_line_start='· ')



# 12 Prompts (eg password)
from rich.prompt import Prompt

Prompt.ask("Enter any of the values ", password=False, choices=['a','b'], show_choices=True) # password=False means all you type is shown at the prompt

password = Prompt.ask("Enter a password", password=True, show_default=False, console=None) # password=True means all you type isn't shown at the prompt




# 99 Animated table (defective)
import contextlib
import json
import time
from pathlib import Path
from rich.console import Console
from rich.live import Live
from rich.table import Table

console = Console()
coins = coin = ""
num_coins = 1

def make_table(coin_list):
    """Generate a Rich table from a list of coins"""
    table = Table(
        title=f"Crypto Data - {time.asctime()}",
        style="black on grey66",
        header_style="white on dark_blue",
    )
    table.add_column("Symbol")
    table.add_column("Name", width=30)
    table.add_column("Price (USD)", justify="right")
    table.add_column("Volume (24h)", justify="right", width=16)
    table.add_column("Percent Change (7d)", justify="right", width=8)
    for coin in coin_list:
        symbol, name, price, volume, pct_change = (
            coin["symbol"],
            coin["name"],
            coin["price_usd"],
            f"{coin['volume24']:.2f}",
            float(coin["percent_change_7d"]),
        )
        pct_change_str = f"{pct_change:2.1f}%"
        if pct_change > 5.0:
            pct_change_str = f"[white on dark_green]{pct_change_str:>8}[/]"
        elif pct_change < -5.0:
            pct_change_str = f"[white on red]{pct_change_str:>8}[/]"
        table.add_row(symbol, name, price, volume, pct_change_str)
    return table

# Load the coins data
raw_data = json.loads(Path("crypto_data.json").read_text(encoding="utf-8")) # find a input file that matches these cols' data type and has enough records for the table to scroll new data for a while
num_coins = int(len(raw_data))
coins = raw_data + raw_data
num_lines = 20

with Live(make_table(coins[:num_lines]), screen=True) as live:
    index = 0
    with contextlib.suppress(KeyboardInterrupt):
        while True:
            live.update(make_table(coins[index : index + num_lines]))
            time.sleep(0.5)
            index = (index + 1) % num_coins
import requests
from rich.console import Console
from rich.panel import Panel


def get_random_quote():
    # Fetch a random quote from a free public API
    url = "https://dummyjson.com/quotes/random"
    response = requests.get(url)
    data = response.json()

    return data["quote"], data["author"]


def main():
    console = Console()

    try:
        quote, author = get_random_quote()

        # Display the quote in a pretty panel
        console.print(
            Panel(
                f"[bold italic]{quote}[/bold italic]\n\n— {author}",
                title="Random Quote",
                expand=False,
            )
        )
    except Exception as e:
        console.print(f"[red]Error fetching quote: {e}[/red]")


if __name__ == "__main__":
    main()

import wikipedia


def main():
    """Get user input for page title and display the title, summary and url of the page."""
    page_title = input("Page title: ")
    while page_title:
        try:
            searched_result = wikipedia.page(page_title)
            print(f"Title: {searched_result.title}")
            print(f"Summary: {searched_result.summary}")
            print(f"URL: {searched_result.url}")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f"{page_title} cannot be found. Try another page.")
        page_title = input("Page title: ")


main()

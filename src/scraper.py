import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
MAX_PAGES = 5
OUTPUT_FILE = "data/products.csv"


def scrape_books():
    """Scrape book details from multiple pages."""

    books = []
    current_url = BASE_URL
    page_number = 1

    while current_url and page_number <= MAX_PAGES:
        print(f"Scraping page {page_number}...")

        try:
            response = requests.get(
                current_url,
                timeout=10
            )
            response.raise_for_status()

        except requests.RequestException as error:
            print(
                f"Error while scraping page "
                f"{page_number}: {error}"
            )
            break

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        book_items = soup.select(
            "article.product_pod"
        )

        for book in book_items:

            # Extract book title
            title = book.h3.a.get(
                "title",
                ""
            ).strip()

            # Extract price
            price_element = book.select_one(
                ".price_color"
            )

            if price_element:
                price = price_element.get_text(
                    strip=True
                )
            else:
                price = "N/A"

            # Extract rating
            rating_element = book.select_one(
                ".star-rating"
            )

            rating = "N/A"

            if rating_element:
                rating_classes = rating_element.get(
                    "class",
                    []
                )

                rating_names = {
                    "One": 1,
                    "Two": 2,
                    "Three": 3,
                    "Four": 4,
                    "Five": 5
                }

                for name, value in rating_names.items():
                    if name in rating_classes:
                        rating = value
                        break

            # Extract availability
            availability_element = book.select_one(
                ".availability"
            )

            if availability_element:
                availability = availability_element.get_text(
                    " ",
                    strip=True
                )
            else:
                availability = "N/A"

            # Store book information
            books.append(
                {
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "Availability": availability
                }
            )

        # Find the next page
        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:
            next_page = next_button.get(
                "href"
            )

            current_url = urljoin(
                current_url,
                next_page
            )

            page_number += 1

        else:
            current_url = None

    return books


def save_to_csv(books):
    """Save scraped books to a CSV file."""

    if not books:
        print("No books were scraped.")
        return

    dataframe = pd.DataFrame(books)

    dataframe.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"\nSuccessfully scraped "
        f"{len(dataframe)} books."
    )

    print(
        f"Data saved to: {OUTPUT_FILE}"
    )


def main():
    """Run the web scraper."""

    books = scrape_books()
    save_to_csv(books)


if __name__ == "__main__":
    main()
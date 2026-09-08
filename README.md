# Web Scraping and Data Extraction

A Python-based web scraping project that extracts structured book information from Books to Scrape and exports the collected data into a CSV file.

## Features

- Scrapes book information from multiple pages
- Extracts book titles
- Extracts prices
- Extracts ratings
- Extracts availability status
- Handles pagination automatically
- Includes HTTP error handling
- Uses request timeouts
- Stores the scraped data in CSV format
- Uses Pandas for structured data processing

## Technologies Used

- Python 3
- Requests
- BeautifulSoup
- Pandas

## Project Structure

```text
CODECRAFT_SD_05/
│
├── data/
│   └── books.csv
│
├── src/
│   └── scraper.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── venv/
```

> The `venv/` directory is excluded from GitHub using `.gitignore`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Varshamadhavan1403/CODECRAFT_SD_05.git
cd CODECRAFT_SD_05
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper using:

```bash
python src/scraper.py
```

The program scrapes up to five pages and saves the results to:

```text
data/books.csv
```

## Sample Output

The generated CSV contains the following fields:

```text
Title
Price
Rating
Availability
```

Example:

| Title | Price | Rating | Availability |
|---|---|---:|---|
| A Light in the Attic | £51.77 | 3 | In stock |
| Tipping the Velvet | £53.74 | 1 | In stock |

## How It Works

The scraper follows these steps:

1. Sends an HTTP request to the target website using Requests.
2. Parses the returned HTML using BeautifulSoup.
3. Identifies book elements using CSS selectors.
4. Extracts title, price, rating, and availability.
5. Follows the pagination links to scrape additional pages.
6. Stores the extracted information in a Python list.
7. Converts the data into a Pandas DataFrame.
8. Exports the structured data to a CSV file.

## Error Handling

The scraper includes:

- HTTP status validation
- Request timeout handling
- Missing HTML element handling
- Graceful termination when scraping errors occur

## Data Source

This project uses **Books to Scrape**, a website created specifically for practicing web scraping.

Website:

https://books.toscrape.com/

## Internship Task

This project was developed as part of the CodeCraft Infotech Software Development Internship Program.

**Task:** Task 05 – Web Scraping

## Author

Varsha Madhavan
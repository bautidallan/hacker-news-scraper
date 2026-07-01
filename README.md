# 🕷️ Hacker News Scraper

A Python web scraper that extracts the top stories from [Hacker News](https://news.ycombinator.com/), including titles, links, and points — across multiple pages — and exports the results to a CSV file with a summary report.

---

## 📌 Features

- Scrapes multiple pages of Hacker News (default: 3 pages = ~90 stories)
- Extracts title, link, and points for each story
- Handles posts without points (e.g. job listings)
- Exports results to `noticias.csv`
- Prints a summary report in the console

---

## 🛠️ Tech Stack

- Python 3
- [requests](https://pypi.org/project/requests/) — HTTP requests
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) — HTML parsing
- [pandas](https://pypi.org/project/pandas/) — CSV export

---

## ▶️ How to run

1. Clone the repository:
```bash
git clone https://github.com/TU_USUARIO/hacker-news-scraper.git
cd hacker-news-scraper
```

2. Install dependencies:
```bash
pip install requests beautifulsoup4 pandas
```

3. Run the scraper:
```bash
python scrap.py
```

---

## 📊 Sample output

```
La peticion fue exitosa
La peticion fue exitosa
La peticion fue exitosa
90 noticias guardadas en noticias.csv

📊 Reporte:
   Total de noticias: 90
   Promedio de puntos: 87.3
   Noticia más popular: Show HN: I built a tool that...
   Puntos: 643
```

---

## 📁 CSV output

| title | link | point |
|---|---|---|
| Show HN: I built a tool... | https://ejemplo.com | 643 |
| Ask HN: Best resources? | https://otro.com | 412 |

---

## 🧠 What I learned

- How to make HTTP requests with a User-Agent header to avoid blocks
- How to parse and navigate HTML with BeautifulSoup
- Recursive pagination to scrape multiple pages
- How to handle missing data gracefully (`score_tag else 0`)
- Exporting structured data to CSV with pandas

---

## ⚠️ Notes

- This project was built for learning purposes
- Hacker News data is public and scraping is allowed per their guidelines
- Some stories (job posts) don't have points and are recorded as 0

---

*Built by Bauti — CS Student @ Mar del Plata 🇦🇷*

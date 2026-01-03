import pandas as pd
import random
import markdown
import pdfkit
import platform


def get_book_genre(book_name: str) -> str:

    df = pd.read_csv("Goodreads_books_with_genres.csv")
    genre = df[df.Title.str.contains(book_name)]["genres"].values.tolist()[0].split(";")
    genre = genre[random.randint(0, len(genre))]
    return genre


def create_md(text, title):
    with open(f"{title}.md", "w") as f:
        f.write(f"# Title: {title}")
        f.write(r"\n")
        for x in range(len(text)):
            f.write("\n")
            f.write(f"## Chapter {x+1}")
            f.write("\n")
            f.write(text[x])
    return title

 

def convert(filename):
    with open(f"{filename}.md", "r") as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(f"{filename}.html", "w", encoding="utf-8") as f:
        f.write(html)
    return f"{filename}"

from weasyprint import HTML
import platform

def to_pdf(filename):
    html_file = f"{filename}.html"
    pdf_file = f"{filename}.pdf"

    # Convert HTML to PDF using WeasyPrint (cross-platform, no need for external binaries)
    HTML(html_file).write_pdf(pdf_file)

    return pdf_file

import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        return None

def extract_article_title(soup):
    title = soup.find("h1", {"class": "firstHeading"}).text
    return title

def extract_article_content(soup):
    content = {}
    paragraphs = soup.find_all("p")
    current_heading = None
    for p in paragraphs:
        if p.find("span", {"class": "mw-headline"}):
            current_heading = p.find("span", {"class": "mw-headline"}).text
            content[current_heading] = ""
        if current_heading:
            content[current_heading] += p.text
    return content

def extract_links_to_other_pages(soup):
    links = []
    for link in soup.find_all("a", href=True):
        if link["href"].startswith("/wiki/"):
            links.append(link["href"])
    return links

def scrape_wikipedia_page(url):
    html_content = get_html_content(url)
    if html_content:
        soup = BeautifulSoup(html_content, "html.parser")
        
        title = extract_article_title(soup)
        content = extract_article_content(soup)
        links = extract_links_to_other_pages(soup)
        
        result = {
            "title": title,
            "content": content,
            "links": links
        }
        return result
    else:
        return None

wiki_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
result = scrape_wikipedia_page(wiki_url)
print(result)

import requests
from bs4 import BeautifulSoup

def get_article_text(url):
    """Fetches the article text from the given URL."""
    try:
        # Send GET request to the article URL
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the article body using the provided class which took a bit to find via inspecting html elements
        article_body = soup.find('div', class_='single__content entry-content m-bottom')

        # If found, return the article text
        if article_body:
            return article_body.get_text(strip=True)
        else:
            print("Error: Article body not found.")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")
        return ""

def count_word_in_article(article_text, word):
    """Counts how many times a word appears in the article text."""
    word_count = article_text.lower().count(word.lower())  # Case-insensitive count
    return word_count

def main():
    # Article URL
    url = 'https://nypost.com/2024/11/28/us-news/mass-arrests-at-macys-thanksgiving-day-parade-as-anti-israel-protesters-block-path/'

    # Fetch the article text
    article_text = get_article_text(url)

    if article_text:
        # Count how many times the word "Israel" appears
        word_to_count = "Israel"
        count = count_word_in_article(article_text, word_to_count)
        print(f"The word '{word_to_count}' appears {count} times in the article.")

if __name__ == "__main__":
    main()

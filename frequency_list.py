import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def get_word_frequency(wikipedia_url):
    try:
        # Fetch the Wikipedia page
        response = requests.get(wikipedia_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        html_content = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the main content of the page
        content_div = soup.find('div', {'class': 'mw-parser-output'})
        if not content_div:
            print("Could not find the main content on the page.")
            return None

        # Get all text within the content
        text = content_div.get_text()

        # Remove punctuation and non-alphabetic characters, convert to lowercase
        words = re.findall(r'\b[a-z]+\b', text.lower())

        # Count word frequencies
        word_frequencies = Counter(words)

        # Return the frequencies sorted by most common
        return word_frequencies.most_common()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
wikipedia_link = input("Enter the Wikipedia page URL: ")
word_frequencies = get_word_frequency(wikipedia_link)

if word_frequencies:
    print("\nWord Frequencies:")
    print(len(word_frequencies))
    for word, count in word_frequencies[:50]:  # Show top 100 words
        print(f"{word}: {count}")

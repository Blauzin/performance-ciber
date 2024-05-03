import requests 
import threading

import requests
from bs4 import BeautifulSoup

def extract_first_paragraph_and_links(url, file_path):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        first_paragraph = soup.find('p')
        if first_paragraph:
            paragraph_text = first_paragraph.get_text()
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(paragraph_text)
            links = [a['href'] for a in first_paragraph.find_all('a', href=True)]
            
            return links
        else:
            return "No paragraph found", []
    else:
        return f"Failed to retrieve the webpage, status code: {response.status_code}", []

# Example usage:
url = "https://pt.wikipedia.org/wiki/Web_scraping"
text, links = extract_first_paragraph_and_links(url)
print("Text:", text)
print("Links:", links)


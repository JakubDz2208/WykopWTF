import requests
from bs4 import BeautifulSoup
import pandas as pd

class CommentScraper:
    def __init__(self, url, comments_selector):
        self.comments_selector = comments_selector
        self.comments_df = pd.DataFrame(columns=['Comment'])
        self.base_url = "https://wykop.pl"
        self.url = self.base_url + "/tag/" + str(url)

    def get_page_content(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            return None

    def click_more_buttons(self, soup):
        more_buttons = soup.select('.more')
        for more_button in more_buttons:
            if callable(getattr(more_button, 'click', None)):
                more_button.click()

    def scrape_comments_on_page(self, soup, limit):
        self.click_more_buttons(soup)  # Click all "more" buttons if they exist

        comments = soup.select(self.comments_selector)
        for comment in comments:
            comment_text = comment.get_text(strip=True)
            self.comments_df = pd.concat([self.comments_df, pd.DataFrame([{"Comment": comment_text}])], ignore_index=True)

    def scrape_comments(self, url=None, limit=None):
        url = self.url

        while len(self.comments_df) < limit:
            page_content = self.get_page_content(url)

            if not page_content:
                break

            soup = BeautifulSoup(page_content, 'html.parser')
            self.scrape_comments_on_page(soup, limit)

            # Find the next page link dynamically
            next_page_link = soup.select_one('.new-pagination li.next a')

            if next_page_link:
                next_page_url = self.base_url + next_page_link.get('href')
                url = next_page_url
            else:
                break

        return self.comments_df[:limit]

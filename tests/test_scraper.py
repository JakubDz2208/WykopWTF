from unittest.mock import Mock
from pytest import mark
from scraper.scraper import CommentScraper
from bs4 import BeautifulSoup


@mark.scraper
def test_get_page_content_success(mock_requests_get):
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.text = "Mocked HTML Content"

    scraper = CommentScraper("example-tag", ".comment-selector")
    result = scraper.get_page_content("example.com")

    assert result == "Mocked HTML Content"


@mark.scraper
def test_get_page_content_failure(mock_requests_get):
    mock_requests_get.return_value.status_code = 404

    scraper = CommentScraper("example-tag", ".comment-selector")
    result = scraper.get_page_content("example.com")

    assert result is None


@mark.scraper
def test_click_more_buttons():
    mock_button = Mock()
    mock_button.click = Mock()

    soup = BeautifulSoup("<div class='more'></div>", 'html.parser')
    soup.select = Mock(return_value=[mock_button])

    scraper = CommentScraper("example-tag", ".comment-selector")
    scraper.click_more_buttons(soup)

    mock_button.click.assert_called_once()


@mark.scraper
def test_scrape_comments_on_page():
    soup = BeautifulSoup("<div class='comment-selector'>Comment 1</div>", 'html.parser')

    scraper = CommentScraper("example-tag", ".comment-selector")
    scraper.scrape_comments_on_page(soup, 1)

    assert len(scraper.comments_df) == 1
    assert scraper.comments_df.iloc[0]['Comment'] == "Comment 1"

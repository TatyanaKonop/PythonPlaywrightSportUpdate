import time
import pytest

from pages.external_page.calendar_result_page import CalendarResultPage
from pages.home_page import HomePage
from pages.menu_orient_Internal_page import OrientInternal
from pages.search_page import SearchPage
from pages.three_search_format_page import ThreeSearchFormatPage


@pytest.mark.parametrize('search_data, text_in_input', [('Elena', "")])
def test_search(
    search_data: str,
    text_in_input: str,
    browser
):
    TEXT_SEARCH_LINE_RESULT = "Search results for '{search_data}'".format(search_data=search_data)
    URI = ""
    home_page = HomePage(browser)
    home_page.open(URI)
    home_page.search.find_result(
         search_data
     )
    search_page = SearchPage(browser, search_data=search_data)
    search_page.text_search_present(TEXT_SEARCH_LINE_RESULT)

def test_navigate_sidebar( browser):
    #sections_text = ['Internal', 'Event Advising', 'List']
    sections_text_sidebar = ['Internal', 'Foot Orienteering Commission', '3rd Sprint Format: Knock-Out Sprint']
    SECTION_TEXT_NAVBAR = ['Orienteering', 'Internal']
    URI = ""
    home_page = HomePage(browser)
    home_page.open(URI)
    home_page.navbar.navigate_to_section_on_main_menu(SECTION_TEXT_NAVBAR)
    orient_internal_page = OrientInternal(browser)
    orient_internal_page.sidebar.navigate_to_section(sections_text_sidebar)
    three_search_format_page = ThreeSearchFormatPage(browser)
    three_search_format_page.text_search_present(sections_text_sidebar[-1])

def test_navigate_on_top_menu(browser):
    SECTION_TEXT_NAVBAR_TOP_MENU = ['Calendar & Results']
    LIST_FILTER = [
        {"Event type": ["National Event", "Partner Event", "World Cup"]},
        {"Regions": ["Africa", "Asia"]},
        {"Disciplines": ["FootO", "TrailO"]},
        {"Competition format": ["Mass start"]}
    ]

    URI = ""
    home_page = HomePage(browser)
    home_page.open(URI)
    page = home_page.navbar.navigate_to_section_on_top_menu(SECTION_TEXT_NAVBAR_TOP_MENU)
    calendar_result_page = CalendarResultPage(page)
    calendar_result_page.event_calendar.filter(LIST_FILTER)
    calendar_result_page.text_filtered_present(LIST_FILTER)
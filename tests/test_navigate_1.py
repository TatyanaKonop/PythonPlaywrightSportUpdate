import time
import pytest

from pages.external_page.calendar_result_page import CalendarResultPage
from pages.home_page import HomePage
from pages.menu_orient_Internal_page import OrientInternal
from pages.search_page import SearchPage
from pages.three_search_format_page import ThreeSearchFormatPage


def test_filter_data_on_table(browser):
    SECTION_TEXT_NAVBAR_TOP_MENU = ['Calendar & Results']
    LIST_FILTER = [
        {"Regions": ["Europe"]},
        {"Disciplines": ["TrailO"]}
    ]
    URI = ""
    home_page = HomePage(browser)
    home_page.open(URI)
    page = home_page.navbar.navigate_to_section_on_top_menu(SECTION_TEXT_NAVBAR_TOP_MENU)
    calendar_result_page = CalendarResultPage(page)
    calendar_result_page.event_calendar.filter(LIST_FILTER)
    calendar_result_page.table.check_data_from_table_and_filtred_items(LIST_FILTER, "Regions")

    time.sleep(5)



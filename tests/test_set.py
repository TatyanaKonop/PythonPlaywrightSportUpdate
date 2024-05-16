import uuid
import pytest
import allure
from pages.external_page.calendar_result_page import CalendarResultPage
from pages.home_page import HomePage
from pages.menu_orient_Internal_page import OrientInternal
from pages.search_page import SearchPage
from pages.three_search_format_page import ThreeSearchFormatPage

unique_id = str(uuid.uuid4())


# @allure.feature("Search Functionality")
# @allure.story("Search data throw search input")
# @allure.id(unique_id)
# @allure.severity(allure.severity_level.NORMAL)
# @allure.description(
#     "Test that verifies a user  inputs data in search field and on the search results page a search result block is displayed")
# @pytest.mark.regression
# @pytest.mark.parametrize('search_data, text_in_input', [('Elena', "")])
# def test_search(
#         search_data: str,
#         text_in_input: str,
#         browser
# ):
#     TEXT_SEARCH_LINE_RESULT = "Search results for '{search_data}'".format(search_data=search_data)
#     URI = ""
#     home_page = HomePage(browser)
#     home_page.open(URI)
#     home_page.search.find_result(
#         search_data
#     )
#     search_page = SearchPage(browser, search_data=search_data)
#     search_page.text_search_present(TEXT_SEARCH_LINE_RESULT)


@allure.feature("Navigation")
@allure.story("Navigate to search information")
@allure.id(unique_id)
@allure.severity(allure.severity_level.NORMAL)
@allure.description(
    "Test that verifies a user navigates throw main menu and sidebar and on the search results page a search result block is displayed")
@pytest.mark.parametrize('shard', [1, 2, 3, 4])
@pytest.mark.regression
def test_navigate_sidebar(shard, browser):
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


# @allure.feature("Filtration")
# @allure.story("Use filter to find information")
# @allure.id(unique_id)
# @allure.severity(allure.severity_level.NORMAL)
# @allure.description(
#     "Test that verifies a user  filters  and on the search results page a search result block is displayed")
# @pytest.mark.regression
# def test_filter(browser):
#     SECTION_TEXT_NAVBAR_TOP_MENU = ['Calendar & Results']
#     LIST_FILTER = [
#         {"Event type": ["National Event", "Partner Event", "World Cup"]},
#         {"Regions": ["Africa", "Asia"]},
#         {"Disciplines": ["FootO", "TrailO"]},
#         {"Competition format": ["Mass start"]}
#     ]

#     URI = ""
#     home_page = HomePage(browser)
#     home_page.open(URI)
#     page = home_page.navbar.navigate_to_section_on_top_menu(SECTION_TEXT_NAVBAR_TOP_MENU)
#     calendar_result_page = CalendarResultPage(page)
#     calendar_result_page.event_calendar.filter(LIST_FILTER)
#     calendar_result_page.text_filtered_present(LIST_FILTER)


# @allure.feature("Filtration")
# @allure.story("Use filter to find information")
# @allure.id(unique_id)
# @allure.severity(allure.severity_level.NORMAL)
# @allure.description(
#     "Test that verifies a user  filters  and on the search results page a search result  is displayed in the table")
# @pytest.mark.regression
# def test_filter_data_on_table(browser):
#     SECTION_TEXT_NAVBAR_TOP_MENU = ['Calendar & Results']
#     LIST_FILTER = [
#         {"Regions": ["Europe"]},
#         {"Disciplines": ["TrailO"]}
#     ]
#     URI = ""
#     home_page = HomePage(browser)
#     home_page.open(URI)
#     page = home_page.navbar.navigate_to_section_on_top_menu(SECTION_TEXT_NAVBAR_TOP_MENU)
#     calendar_result_page = CalendarResultPage(page)
#     calendar_result_page.event_calendar.filter(LIST_FILTER)
#     calendar_result_page.table.check_data_from_table_with_filtered_item(LIST_FILTER, "Regions")


# @allure.feature("Filtration")
# @allure.story("Use calendar to filter and to find information")
# @allure.id(unique_id)
# @allure.severity(allure.severity_level.NORMAL)
# @allure.description(
#     "Test that verifies a user  choses a start  month which is ahead of  an end  month  and the end  month is changed automatically")
# @pytest.mark.regression
# def test_automatically_change_month_on_calendar(browser):
#     SECTION_TEXT_NAVBAR_TOP_MENU = ['Calendar & Results']
#     URI = ""
#     home_page = HomePage(browser)
#     home_page.open(URI)
#     page = home_page.navbar.navigate_to_section_on_top_menu(SECTION_TEXT_NAVBAR_TOP_MENU)
#     calendar_result_page = CalendarResultPage(page)
#     calendar_result_page.event_calendar.open_calendar()
#     calendar_result_page.calendar.check_calendar_automatically_change_end_month_if_start_data_ahead(
#         'May')  # Pass name of month ahead of current month

import bs4
import requests

BASE_URL = "https://assessments.milwaukee.gov"
BUILDING_TYPE_ENDPOINT = "search-middle-ns.asp"
SEARCH_RESULTS_ENDPOINT = "SearchResults.asp"


# Get the list of building types.
def get_building_types():
    response = requests.get(f"{BASE_URL}/{BUILDING_TYPE_ENDPOINT}")
    bs = bs4.BeautifulSoup(response.content.decode(), features="html.parser")
    el = bs.find(id="SelectBuildingType")
    options = el.find_all("option")
    building_types = list()
    for option in options:
        if option.text:
            building_types.append((option["value"], option.text))
    for k, v in building_types:
        print(f"{k}: {v}")


# Get all the results from a single results page
def get_search_results(building_type: str, year: int):
    form_data = dict(SearchBuildingType=building_type, SearchYearBuilt=year, SearchYearBuiltThru=year)
    response = requests.post(f"{BASE_URL}/{SEARCH_RESULTS_ENDPOINT}", data=form_data)
    bs = bs4.BeautifulSoup(response.content.decode(), features="html.parser")
    table = bs.find(id="T1")
    header_row = table.find("thead").find("tr")
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        print("Hi")

    for row in rows[1:]:
        print("Hi")

# For each building type, cycle through every year from 1900-2022

# Store results in a database

# Something else reads database and scrapes each listing, saves to a different table


# Main
# building_types = get_building_types()
get_search_results("Duplex O/S", 1900)

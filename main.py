# Main file for busChecker app
from bs4 import BeautifulSoup
import requests


def main():
    bus_number = "408"
    bus_schedule_url = "https://busstops.aacps.org/public/BusRouteIssues.aspx"

    page = requests.get(bus_schedule_url)
    scraped_data = BeautifulSoup(page.text, 'html.parser')

    if scraped_data.find(bus_number):
        print("The bus isn't running.")
    else:
        print("The bus is running.")


if __name__ == "__main__":
    main()

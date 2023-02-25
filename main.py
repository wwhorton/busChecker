# Main file for busChecker app
from bs4 import BeautifulSoup
import requests
import yagmail


def main():
    bus_number = "408"
    bus_schedule_url = "https://busstops.aacps.org/public/BusRouteIssues.aspx"
    page = requests.get(bus_schedule_url)
    scraped_data = BeautifulSoup(page.text, 'html.parser')

    if scraped_data.find(bus_number):
        notify("Eliza's bus isn't running.")

    else:
        notify("Eliza's bus is running.")


def notify(status):
    oath2_source = "./client_secret_1097203586936-1spn72t38cco4qf3mmm5vbl3d1haj4o8.apps.googleusercontent.com.json"
    receivers = ["whorton@gmail.com", "agreenwhorton@gmail.com"]

    yag = yagmail.SMTP("whorton@gmail.com", oauth2_file=oath2_source)
    yag.send(
        to=receivers,
        subject="Schoolbus Disruption",
        contents=status
    )


if __name__ == "__main__":
    main()

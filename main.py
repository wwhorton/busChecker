# Main file for busChecker app
from bs4 import BeautifulSoup
import time
import requests
import yagmail
from datetime import datetime
import atexit
from signal import signal, SIGINT, SIGTERM, SIGKILL


def main():
    bus_number = "408"
    bus_schedule_url = "https://busstops.aacps.org/public/BusRouteIssues.aspx"
    page = requests.get(bus_schedule_url)
    scraped_data = BeautifulSoup(page.text, 'html.parser')
    email_sent = False
    time_format = "%H:%M"
    current_time = time.localtime()
    current_time_formatted = time.strftime(time_format)
    start_time = time.strptime("07:00", time_format)
    end_time = time.strptime("14:00", time_format)

    send_start_message(current_time_formatted)

    while True:
        if datetime.today().weekday() < 5:
            while start_time < current_time < end_time:
                if current_time.tm_min is 00 and email_sent is False:
                    email_sent = check_bus(bus_number, scraped_data)


def notify(subject, status):
    oath2_source = "./client_secret_1097203586936-1spn72t38cco4qf3mmm5vbl3d1haj4o8.apps.googleusercontent.com.json"
    receivers = ["whorton@gmail.com"]

    yag = yagmail.SMTP("whorton@gmail.com", oauth2_file=oath2_source)
    yag.send(
        to=receivers,
        subject=subject,
        contents=status
    )


def send_start_message(msg_time):
    notify("Bus Checker is running", "Bus Checker just started at " + msg_time)


@atexit.register
def send_exit_message():
    notify("Bus Checker exited", "Bus Checker exited at " + time.localtime().strftime("%H:%M"))


signal(SIGINT, send_exit_message)
signal(SIGTERM, send_exit_message)
signal(SIGKILL, send_exit_message)


def check_bus(bus_number, scraped_data):
    if bus_number in scraped_data is True:
        notify("Schoolbus Disruption", "Eliza's bus isn't running.")
        return True


if __name__ == "__main__":
    main()

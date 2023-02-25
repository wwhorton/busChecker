# Bus Checker
Python script to check if a school bus is running and notify if it isn't.

On launch and exit it sends an email to notify that it has started or ended. It uses BeautifulSoup to scrape the URL for our county's public school bus disruption notification page, then searches for the bus number. If found, it emails a notification.

It's set to scrape hourly on weekdays between the hours of 7 and 2. It uses an oAuth2 file and the yagmail library to handle the email. 

It runs as a terminal process and exits gracefully on CTRL+C.

## To Do (_in no particular order_)

- Get variable values from user inputs on launch
- Optionally take variables from a config file
- Testing
- GUI
- Allow for separate admin and notification email addresses, so that launch and quit is sent to one address but notifications are sent to the other


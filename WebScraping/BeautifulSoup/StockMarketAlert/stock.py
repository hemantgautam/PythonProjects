def get_stock_alert():
    import requests
    from bs4 import BeautifulSoup
    from twilio.rest import Client

    scrape_url = 'https://www.google.com/search?client=firefox-b-d&q=delta+corp+price'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    page = requests.get(scrape_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    raw_price = soup.find_all("span", class_="IsqQVc")
    stock_name = raw_price[0].get_text()
    stock_price = raw_price[1].get_text()

    account_sid = '<Enter Your Twilio Account SID>'
    auth_token = '<Enter You Twilio Account Token>'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=stock_name + ": " + stock_price,
        to='whatsapp:+918792564177'
    )
    print(message)


get_stock_alert()

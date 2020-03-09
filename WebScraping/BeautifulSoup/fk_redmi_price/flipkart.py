# This function make request to given url and fetch html content using beautiful soup
# and using soup.findall function gets the exact product name and its price
def check_myntra_product_price():
    import requests
    from bs4 import BeautifulSoup
    # global discounted_price
    # global product_name
    scrape_url = "https://www.flipkart.com/realme-c2-diamond-black-32-gb/p/itmfgwba8kmejqpe?pid=MOBFHBZ4MDMCNHNK&lid=LSTMOBFHBZ4MDMCNHNKOFORJ3&marketplace=FLIPKART&srno=b_1_5&otracker=clp_metro_expandable_1_4.metroExpandable.METRO_EXPANDABLE_mobile-phones-store_25DMXHG2C5AT_wp3&fm=organic&iid=3892a3ab-75ba-433c-b2ae-d72032196d40.MOBFHBZ4MDMCNHNK.SEARCH&ssid=gw3074joyo0000001581513118690"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    page = requests.get(scrape_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    raw_price = soup.find_all("div", class_='_1vC4OE _3qQ9m1')
    raw_product_name = soup.find_all("span", class_='_35KyD6')

    for pn in raw_product_name:
        product_name = pn
    product_name = product_name.get_text()
    product_name = product_name.encode('ascii', 'ignore')

    for rp in raw_price:
        discounted_price = rp
    discounted_price = discounted_price.get_text().replace(",", "")
    discounted_price = int(discounted_price[1:])
    # If this condition is True than email gets triggered
    if discounted_price < 5000:
        send_email(product_name, discounted_price, scrape_url)
    else:
        print("Price is still more than 5000")

#This function sends email to email id with new discounted price and link
def send_email(product_name, discounted_price, scrape_url):
    import time
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('enter you emailid', 'enter your password')
    subject = "Flipkart Product Price Came Down"
    body = "New Price for this product is: " + str(discounted_price) + "\n" + str(
        product_name) + "\n\n" + "Click on this URL to access\n" + scrape_url
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'enter from email id',
        'enter to email id',
        msg
    )
    print("Email is sent")
    time.time()
    server.quit()


check_myntra_product_price()

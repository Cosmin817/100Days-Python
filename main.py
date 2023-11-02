import requests
from itertools import islice
from twilio.rest import Client

def deviation_percentage_calc(yesterday_closing_price: float, before_yesterday_closing_price: float) -> dict:
    global direction
    difference: float = yesterday_closing_price - before_yesterday_closing_price
    percentage: float = (difference / before_yesterday_closing_price) * 100
    if percentage < 0:
        f_direction = "🔻"
    elif percentage > 0:
        f_direction = "🟢"
    else:
        f_direction = "⏸"
    output = {'percentage_deviation': abs(percentage), 'stock_direction': f_direction}
    return output


def get_news() -> dict:
    #FULL URL: https://newsapi.org/v2/top-headlines?q=TESLA&pageSize=3&apiKey=9b3163e9f1074d3eb3b7cfa6a5d67522
    get_news_parameters = {
        'q': COMPANY_NAME,
        'pageSize': 3,
        'apikey': NEWS_API_KEY,
        'sortBy': "publishedAt",
        'language': "en"
    }
    news_request = requests.get(url="https://newsapi.org/v2/everything", params=get_news_parameters)
    news_json = news_request.json()
    print(news_request.url)
    title_dict = {}
    for article in news_json['articles']:
        title_dict[article['title']] = article['description']
    return title_dict


def send_sms(stock_symbol: str, stock_data: dict, stock_direction: str):
    account_sid = 'ACb3ecdfb36ca582b3888fb1a11c62af5f'
    auth_token = '6274fd2ca9387f41703d443bfa41d6f0'

    for heading, description in stock_data.items():
        print(heading)
        print(description)
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+15673722701',
            to='+40749153818',
            body=f'{stock_symbol} {stock_direction} {DEVIATION}%\nHeadline: {heading}\nBrief: {description}',
        )

        print(message.sid)

direction = 'NONE'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "YO3FBR7BQF1KAMDA"
NEWS_API_KEY = "9b3163e9f1074d3eb3b7cfa6a5d67522"
DEVIATION = 3
## STEP 1: Use https://www.alphavantage.co (API_KEY=YO3FBR7BQF1KAMDA)
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&apikey=YO3FBR7BQF1KAMDA

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': API_KEY,
}

#CCH# stock_price_request = requests.get(url="https://www.alphavantage.co/query", params=parameters)
#CCH# stock_price_json = stock_price_request.json()

stock_price_json = {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2023-10-30', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'}, 'Time Series (Daily)': {'2023-10-30': {'1. open': '209.2800', '2. high': '210.8800', '3. low': '194.6700', '4. close': '197.3600', '5. volume': '136448167'}, '2023-10-27': {'1. open': '210.6000', '2. high': '212.4100', '3. low': '205.7700', '4. close': '207.3000', '5. volume': '94881173'}, '2023-10-26': {'1. open': '211.3200', '2. high': '214.8000', '3. low': '204.8800', '4. close': '205.7600', '5. volume': '115112635'}, '2023-10-25': {'1. open': '215.8800', '2. high': '220.1000', '3. low': '212.2000', '4. close': '212.4200', '5. volume': '107065087'}, '2023-10-24': {'1. open': '216.5000', '2. high': '222.0500', '3. low': '214.1100', '4. close': '216.5200', '5. volume': '118231113'}, '2023-10-23': {'1. open': '210.0000', '2. high': '216.9800', '3. low': '202.5100', '4. close': '212.0800', '5. volume': '150683368'}, '2023-10-20': {'1. open': '217.0100', '2. high': '218.8606', '3. low': '210.4200', '4. close': '211.9900', '5. volume': '138010095'}, '2023-10-19': {'1. open': '225.9500', '2. high': '230.6100', '3. low': '216.7800', '4. close': '220.1100', '5. volume': '170772713'}, '2023-10-18': {'1. open': '252.7000', '2. high': '254.6300', '3. low': '242.0800', '4. close': '242.6800', '5. volume': '125147846'}, '2023-10-17': {'1. open': '250.1000', '2. high': '257.1830', '3. low': '247.0800', '4. close': '254.8500', '5. volume': '93562909'}, '2023-10-16': {'1. open': '250.0500', '2. high': '255.3999', '3. low': '248.4800', '4. close': '253.9200', '5. volume': '88917176'}, '2023-10-13': {'1. open': '258.9000', '2. high': '259.6000', '3. low': '250.2200', '4. close': '251.1200', '5. volume': '102296786'}, '2023-10-12': {'1. open': '262.9200', '2. high': '265.4100', '3. low': '256.6307', '4. close': '258.8700', '5. volume': '111508114'}, '2023-10-11': {'1. open': '266.2000', '2. high': '268.6000', '3. low': '260.9000', '4. close': '262.9900', '5. volume': '103706266'}, '2023-10-10': {'1. open': '257.7500', '2. high': '268.9400', '3. low': '257.6500', '4. close': '263.6200', '5. volume': '122656030'}, '2023-10-09': {'1. open': '255.3100', '2. high': '261.3600', '3. low': '252.0500', '4. close': '259.6700', '5. volume': '101377947'}, '2023-10-06': {'1. open': '253.9800', '2. high': '261.6500', '3. low': '250.6500', '4. close': '260.5300', '5. volume': '118121812'}, '2023-10-05': {'1. open': '260.0000', '2. high': '263.6000', '3. low': '256.2500', '4. close': '260.0500', '5. volume': '119159214'}, '2023-10-04': {'1. open': '248.1400', '2. high': '261.8600', '3. low': '247.6000', '4. close': '261.1600', '5. volume': '129721567'}, '2023-10-03': {'1. open': '248.6100', '2. high': '250.0200', '3. low': '244.4500', '4. close': '246.5300', '5. volume': '101985305'}, '2023-10-02': {'1. open': '244.8100', '2. high': '254.2799', '3. low': '242.6200', '4. close': '251.6000', '5. volume': '123810402'}, '2023-09-29': {'1. open': '250.0000', '2. high': '254.7700', '3. low': '246.3500', '4. close': '250.2200', '5. volume': '128522729'}, '2023-09-28': {'1. open': '240.0200', '2. high': '247.5500', '3. low': '238.6500', '4. close': '246.3800', '5. volume': '117058870'}, '2023-09-27': {'1. open': '244.2620', '2. high': '245.3300', '3. low': '234.5800', '4. close': '240.5000', '5. volume': '136597184'}, '2023-09-26': {'1. open': '242.9800', '2. high': '249.5500', '3. low': '241.6601', '4. close': '244.1200', '5. volume': '101993631'}, '2023-09-25': {'1. open': '243.3800', '2. high': '247.1000', '3. low': '238.3100', '4. close': '246.9900', '5. volume': '104636557'}, '2023-09-22': {'1. open': '257.4000', '2. high': '257.7888', '3. low': '244.4800', '4. close': '244.8800', '5. volume': '127524083'}, '2023-09-21': {'1. open': '257.8500', '2. high': '260.8600', '3. low': '254.2100', '4. close': '255.7000', '5. volume': '119951516'}, '2023-09-20': {'1. open': '267.0400', '2. high': '273.9300', '3. low': '262.4606', '4. close': '262.5900', '5. volume': '122514643'}, '2023-09-19': {'1. open': '264.3500', '2. high': '267.8500', '3. low': '261.2000', '4. close': '266.5000', '5. volume': '103704040'}, '2023-09-18': {'1. open': '271.1600', '2. high': '271.4400', '3. low': '263.7601', '4. close': '265.2800', '5. volume': '101543305'}, '2023-09-15': {'1. open': '277.5500', '2. high': '278.9800', '3. low': '271.0000', '4. close': '274.3900', '5. volume': '133692313'}, '2023-09-14': {'1. open': '271.3200', '2. high': '276.7094', '3. low': '270.4200', '4. close': '276.0400', '5. volume': '107709842'}, '2023-09-13': {'1. open': '270.0700', '2. high': '274.9800', '3. low': '268.1000', '4. close': '271.3000', '5. volume': '111673737'}, '2023-09-12': {'1. open': '270.7600', '2. high': '278.3900', '3. low': '266.6000', '4. close': '267.4800', '5. volume': '135999866'}, '2023-09-11': {'1. open': '264.2700', '2. high': '274.8500', '3. low': '260.6100', '4. close': '273.5800', '5. volume': '174667852'}, '2023-09-08': {'1. open': '251.2200', '2. high': '256.5200', '3. low': '246.6700', '4. close': '248.5000', '5. volume': '118559635'}, '2023-09-07': {'1. open': '245.0700', '2. high': '252.8100', '3. low': '243.2650', '4. close': '251.4900', '5. volume': '115312886'}, '2023-09-06': {'1. open': '255.1350', '2. high': '255.3900', '3. low': '245.0600', '4. close': '251.9200', '5. volume': '116959759'}, '2023-09-05': {'1. open': '245.0000', '2. high': '258.0000', '3. low': '244.8600', '4. close': '256.4900', '5. volume': '129469565'}, '2023-09-01': {'1. open': '257.2600', '2. high': '259.0794', '3. low': '242.0100', '4. close': '245.0100', '5. volume': '132541640'}, '2023-08-31': {'1. open': '255.9800', '2. high': '261.1800', '3. low': '255.0500', '4. close': '258.0800', '5. volume': '108861698'}, '2023-08-30': {'1. open': '254.2000', '2. high': '260.5100', '3. low': '250.5900', '4. close': '256.9000', '5. volume': '121988437'}, '2023-08-29': {'1. open': '238.5800', '2. high': '257.4800', '3. low': '237.7700', '4. close': '257.1800', '5. volume': '134047603'}, '2023-08-28': {'1. open': '242.5800', '2. high': '244.3800', '3. low': '235.3500', '4. close': '238.8200', '5. volume': '107673727'}, '2023-08-25': {'1. open': '231.3100', '2. high': '239.0000', '3. low': '230.3500', '4. close': '238.5900', '5. volume': '106612231'}, '2023-08-24': {'1. open': '238.6600', '2. high': '238.9200', '3. low': '228.1801', '4. close': '230.0400', '5. volume': '99777432'}, '2023-08-23': {'1. open': '229.3400', '2. high': '238.9800', '3. low': '229.2900', '4. close': '236.8600', '5. volume': '101077635'}, '2023-08-22': {'1. open': '240.2500', '2. high': '240.8200', '3. low': '229.5500', '4. close': '233.1900', '5. volume': '130597886'}, '2023-08-21': {'1. open': '221.5512', '2. high': '232.1343', '3. low': '220.5800', '4. close': '231.2800', '5. volume': '135702671'}, '2023-08-18': {'1. open': '214.1200', '2. high': '217.5800', '3. low': '212.3600', '4. close': '215.4900', '5. volume': '136276584'}, '2023-08-17': {'1. open': '226.0600', '2. high': '226.7400', '3. low': '218.8300', '4. close': '219.2200', '5. volume': '120718417'}, '2023-08-16': {'1. open': '228.0200', '2. high': '233.9700', '3. low': '225.3800', '4. close': '225.6000', '5. volume': '112484520'}, '2023-08-15': {'1. open': '238.7300', '2. high': '240.5000', '3. low': '232.6100', '4. close': '232.9600', '5. volume': '88197599'}, '2023-08-14': {'1. open': '235.7000', '2. high': '240.6600', '3. low': '233.7500', '4. close': '239.7600', '5. volume': '98595331'}, '2023-08-11': {'1. open': '241.7700', '2. high': '243.7900', '3. low': '238.0200', '4. close': '242.6500', '5. volume': '99038642'}, '2023-08-10': {'1. open': '245.4000', '2. high': '251.8000', '3. low': '243.0000', '4. close': '245.3400', '5. volume': '109498608'}, '2023-08-09': {'1. open': '250.8700', '2. high': '251.1000', '3. low': '241.9000', '4. close': '242.1900', '5. volume': '101596324'}, '2023-08-08': {'1. open': '247.4500', '2. high': '250.9200', '3. low': '245.0100', '4. close': '249.7000', '5. volume': '96642183'}, '2023-08-07': {'1. open': '251.4500', '2. high': '253.6511', '3. low': '242.7600', '4. close': '251.4500', '5. volume': '111097943'}, '2023-08-04': {'1. open': '260.9700', '2. high': '264.7700', '3. low': '253.1100', '4. close': '253.8600', '5. volume': '99539907'}, '2023-08-03': {'1. open': '252.0400', '2. high': '260.4900', '3. low': '252.0000', '4. close': '259.3200', '5. volume': '97829545'}, '2023-08-02': {'1. open': '255.5700', '2. high': '259.5200', '3. low': '250.4900', '4. close': '254.1100', '5. volume': '101752865'}, '2023-08-01': {'1. open': '266.2600', '2. high': '266.4700', '3. low': '260.2500', '4. close': '261.0700', '5. volume': '83645720'}, '2023-07-31': {'1. open': '267.4800', '2. high': '269.0800', '3. low': '263.7800', '4. close': '267.4300', '5. volume': '84582172'}, '2023-07-28': {'1. open': '259.8600', '2. high': '267.2500', '3. low': '258.2312', '4. close': '266.4400', '5. volume': '111446026'}, '2023-07-27': {'1. open': '268.3100', '2. high': '269.1300', '3. low': '255.3000', '4. close': '255.7100', '5. volume': '103697263'}, '2023-07-26': {'1. open': '263.2500', '2. high': '268.0400', '3. low': '261.7500', '4. close': '264.3500', '5. volume': '95856177'}, '2023-07-25': {'1. open': '272.3800', '2. high': '272.9000', '3. low': '265.0000', '4. close': '265.2800', '5. volume': '112757327'}, '2023-07-24': {'1. open': '255.8500', '2. high': '269.8500', '3. low': '254.1200', '4. close': '269.0600', '5. volume': '137005037'}, '2023-07-21': {'1. open': '268.0000', '2. high': '268.0000', '3. low': '255.8000', '4. close': '260.0200', '5. volume': '161796073'}, '2023-07-20': {'1. open': '279.5600', '2. high': '280.9300', '3. low': '261.2000', '4. close': '262.9000', '5. volume': '175158273'}, '2023-07-19': {'1. open': '296.0400', '2. high': '299.2900', '3. low': '289.5201', '4. close': '291.2600', '5. volume': '142355353'}, '2023-07-18': {'1. open': '290.1500', '2. high': '295.2600', '3. low': '286.0100', '4. close': '293.3400', '5. volume': '112434713'}, '2023-07-17': {'1. open': '286.6250', '2. high': '292.2300', '3. low': '283.5700', '4. close': '290.3800', '5. volume': '131569593'}, '2023-07-14': {'1. open': '277.0100', '2. high': '285.3000', '3. low': '276.3100', '4. close': '281.3800', '5. volume': '120062369'}, '2023-07-13': {'1. open': '274.5900', '2. high': '279.4500', '3. low': '270.6000', '4. close': '277.9000', '5. volume': '112681458'}, '2023-07-12': {'1. open': '276.3250', '2. high': '276.5200', '3. low': '271.4600', '4. close': '271.9900', '5. volume': '95672139'}, '2023-07-11': {'1. open': '268.6500', '2. high': '270.9000', '3. low': '266.3700', '4. close': '269.7900', '5. volume': '91972358'}, '2023-07-10': {'1. open': '276.4700', '2. high': '277.5200', '3. low': '265.1000', '4. close': '269.6100', '5. volume': '119425405'}, '2023-07-07': {'1. open': '278.4300', '2. high': '280.7800', '3. low': '273.7700', '4. close': '274.4300', '5. volume': '113879174'}, '2023-07-06': {'1. open': '278.0900', '2. high': '279.9700', '3. low': '272.8800', '4. close': '276.5400', '5. volume': '120707419'}, '2023-07-05': {'1. open': '278.8200', '2. high': '283.8500', '3. low': '277.6000', '4. close': '282.4800', '5. volume': '131530862'}, '2023-07-03': {'1. open': '276.4900', '2. high': '284.2500', '3. low': '275.1100', '4. close': '279.8200', '5. volume': '119685891'}, '2023-06-30': {'1. open': '260.6000', '2. high': '264.4500', '3. low': '259.8900', '4. close': '261.7700', '5. volume': '112620784'}, '2023-06-29': {'1. open': '258.0300', '2. high': '260.7400', '3. low': '253.6100', '4. close': '257.5000', '5. volume': '131283360'}, '2023-06-28': {'1. open': '249.7000', '2. high': '259.8800', '3. low': '248.8900', '4. close': '256.2400', '5. volume': '159770797'}, '2023-06-27': {'1. open': '243.2400', '2. high': '250.3899', '3. low': '240.8500', '4. close': '250.2100', '5. volume': '164968214'}, '2023-06-26': {'1. open': '250.0650', '2. high': '258.3700', '3. low': '240.7000', '4. close': '241.0500', '5. volume': '179990552'}, '2023-06-23': {'1. open': '259.2900', '2. high': '262.4500', '3. low': '252.8000', '4. close': '256.6000', '5. volume': '177460803'}, '2023-06-22': {'1. open': '250.7700', '2. high': '265.0000', '3. low': '248.2500', '4. close': '264.6100', '5. volume': '166875944'}, '2023-06-21': {'1. open': '275.1300', '2. high': '276.9900', '3. low': '257.7800', '4. close': '259.4600', '5. volume': '211797109'}, '2023-06-20': {'1. open': '261.5000', '2. high': '274.7500', '3. low': '261.1200', '4. close': '274.4500', '5. volume': '165611217'}, '2023-06-16': {'1. open': '258.9200', '2. high': '263.6000', '3. low': '257.2091', '4. close': '260.5400', '5. volume': '167915649'}, '2023-06-15': {'1. open': '248.4000', '2. high': '258.9500', '3. low': '247.2900', '4. close': '255.9000', '5. volume': '160171238'}, '2023-06-14': {'1. open': '260.1700', '2. high': '261.5700', '3. low': '250.5000', '4. close': '256.7900', '5. volume': '170575536'}, '2023-06-13': {'1. open': '253.5100', '2. high': '259.6800', '3. low': '251.3400', '4. close': '258.7100', '5. volume': '162384343'}, '2023-06-12': {'1. open': '247.9400', '2. high': '250.9700', '3. low': '244.5900', '4. close': '249.8300', '5. volume': '150740523'}, '2023-06-09': {'1. open': '249.0700', '2. high': '252.4200', '3. low': '242.0200', '4. close': '244.4000', '5. volume': '200242371'}, '2023-06-08': {'1. open': '224.2200', '2. high': '235.2300', '3. low': '223.0100', '4. close': '234.8600', '5. volume': '164489739'}}}

counter = 0
two_days_closing_price = []
# two_days_stock_info = [yesterday closing price, a day before yesterday closing price]

for key, value in stock_price_json['Time Series (Daily)'].items():
    two_days_closing_price.append(float(value['4. close']))
    counter += 1
    if counter >= 2:
        break

deviation_percentage = deviation_percentage_calc(two_days_closing_price[0], two_days_closing_price[1])
deviation_percentage_result = deviation_percentage

## STEP 2: Use https://newsapi.org (API_KEY=9b3163e9f1074d3eb3b7cfa6a5d67522)
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if deviation_percentage_result['percentage_deviation'] >= DEVIATION:
    important_headlines = get_news()
    send_sms(STOCK, important_headlines, deviation_percentage_result['stock_direction'])

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


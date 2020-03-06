import requests
import argparse
import schedule
import time
import pymysql

url = 'https://api.gdax.com'
sym = 'BTC-USD'
conn = pymysql.connect(host='192.168.159.128', port=3306, user='root', passwd='root', db='test_case', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# parser = argparse.ArgumentParser()
# parser.add_argument('base_url', help='this is url')
# parser.add_argument('symbol', help='this is symbol')
# args = parser.parse_args()
# symbol = args.symbol
# base_url = args.base_url

def selectdata(base_url, symbol):
	data = requests.get(f'{base_url}/products/{symbol}/ticker').json()
	price = data['price']
	timestamp = int(time.time()*1000)
	date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	payload = {
		'symbol': str(symbol),
		'price': price,
		'date': str(date)
	}
	print(payload)
	return payload

def savedata():
	data = selectdata(url, sym)
	time.sleep(1)
	sql = f"INSERT INTO price(symbol, price, date) VALUES ('{sym}', {data['price']}, '{data['date']}');"
	cursor.execute(sql)
	conn.commit()

a = 0
schedule.every(1).seconds.do(selectdata, url, sym)
while True:
	if a <= 5:
		schedule.run_pending()
		time.sleep(3)
		a += 1
	else:
		cursor.close()
		conn.close()
		break

if __name__ == '__main__':
	conn = pymysql.connect(host='192.168.159.128', port=3306, user='root', passwd='root', db='test_case',
		charset='utf8')
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
	li = [1,2,'q']
	sql1 = f"INSERT INTO price(symbol, price, date) VALUES ('aaa', {str(li)}, '132');"
	cursor.execute(sql1)
	conn.commit()
	cursor.close()
	conn.close()
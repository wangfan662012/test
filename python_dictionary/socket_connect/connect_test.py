import websocket
import ssl
import sys
import json
import pymysql
import threading

import time

T_OUT = 'stdout'
T_IN = 'stdin'
T_SAVE_FILE = 'save_file'
RUN_CMD = 'python socket_server.py'
db_info = {
	'db': 'kkb-smallcourse-test',
	'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
	'port': 3306,
	'user': 'ccc_test',
	'password': 'ccTsddTTdddAA123!@#'
}

def receive(ws,count = 1):
	datas = []
	#print("Receiving...")
	for i in range(0, count):
		data = ws.recv()
		print(data)
		datas.append(data)
	return datas


def send_run_remote_cmd(ws):
	send(ws, [T_IN, '\r'])


def send_file(ws, path, content):
	msg = [T_SAVE_FILE, path, content]
	send(ws, msg)


def send_text(ws, text):
	msg = [T_IN, text]
	send(ws, msg)


def send(ws, data: list):
	send_data = json.dumps(data)
	#print('sending ... ')
	#print(send_data)
	ws.send_binary(send_data)


def test_code() -> str:
	code = '''print('############## connecting  #################')'''
	return code

def on_message(ws, message):
	print('message: {}'.format(message))

def on_error(ws, error):
	print('error: {}'.format(error))

def on_close(ws):
	print("### closed ###")

def on_open(ws, file_path):
	#print('on_open')
	receive(ws, 2)
	send_file(ws, file_path, test_code())
	send_text(ws, RUN_CMD)
	receive(ws)
	send_run_remote_cmd(ws)
	receive(ws, 2)
	while True:
		receive(ws, 1)

def db_connect():
	conn = pymysql.connect(**db_info)
	cursor = conn.cursor()
	sql = "select id, class_id from small_task where type='program';"
	cursor.execute(sql)
	ids = cursor.fetchmany(size=3)
	print(ids)
	return ids

def socket_connect(url, save_file_path):
	try:
		ws = websocket.create_connection(
			url,
			# print(url),
			on_error=on_error,
			on_message=on_message,
			on_close=on_close,
			sslopt={"cert_reqs": ssl.CERT_NONE}
		)
	except Exception as error:
		print('connect error : ', error)
		sys.exit(1)
	#print("connect ok !")
	on_open(ws, save_file_path)
	ws.close()
	return ws

threads = []

if __name__ == '__main__':
	ids = db_connect()
	for class_id, task_id in ids:
		save_file_path = f'{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/socket_server.py'
		url = f"wss://xiaoke-test.kaikeba.com/program/_websocket/{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1581909712371?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=N6tTtdxDwKntnkW7WAX&workspace={class_id}%2F{task_id}%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw"
		t = threading.Thread(target=socket_connect, args=(url, save_file_path))
		t.start()
		threads.append(t)
		# t.join()
	# print(threading.enumerate())
	# print(threading.activeCount())
	while True:
		print(len(threads), threading.activeCount())
		# for t in threads:
		# 	print('t:{},close: {}'.format(t.name, t.is_alive()))
		time.sleep(5)


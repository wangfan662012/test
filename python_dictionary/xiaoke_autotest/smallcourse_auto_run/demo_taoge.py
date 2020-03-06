
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
RUN_CMD = 'python main.py'
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
		print(data.encode('utf-8'))
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

def on_open(ws, file_path, code):
	#print('on_open')
	receive(ws, 2)
	send_file(ws, file_path, code)
	send_text(ws, RUN_CMD)
	receive(ws)
	send_run_remote_cmd(ws)
	receive(ws, 2)
	while True:
		receive(ws, 1)

def db_connect():
	conn = pymysql.connect(**db_info)
	cursor = conn.cursor()
	sql = "select id, class_id, props from small_task where (type='program' or type='practice') and class_id in (select id from small_class where course_id in ('cbe825fe-8b1d-4cc6-a15a-28ed10f89695', '1394cb1a-96e6-4995-8d8a-ef042030b475'));"
	sql1 = "select id, class_id, props from small_task where id='00850324-6089-47e9-8314-1accb512be78';"
	cursor.execute(sql1)
	ids = cursor.fetchmany(size=1)
	print(ids)
	return ids

def socket_connect(url, save_file_path, code):
	try:
		ws = websocket.create_connection(
			url,
			# print(url),
			sslopt={"cert_reqs": ssl.CERT_NONE}
		)
	except Exception as error:
		print('connect error : ', error)
		sys.exit(1)
	#print("connect ok !")
	on_open(ws, save_file_path, code)
	ws.close()
	return ws

threads = []

if __name__ == '__main__':
	ids = db_connect()
	for class_id, task_id, props in ids:
		save_file_path = f'{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/main.py'
		url = f"wss://xiaoke-test.kaikeba.com/program/_websocket/{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1581909712371?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=N6tTtdxDwKntnkW7WAX&workspace={class_id}%2F{task_id}%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw"
		json_code = json.loads(props)
		code = json_code['code']
		print(code)
		t = threading.Thread(target=socket_connect, args=(url, save_file_path, code))
		t.start()
		#threads.append(t)
		# t.join()
	# print(threading.enumerate())
	# print(threading.activeCount())
	# while True:
	# 	print(len(threads), threading.activeCount())
		# for t in threads:
		# 	print('t:{},close: {}'.format(t.name, t.is_alive()))
		# time.sleep(5)


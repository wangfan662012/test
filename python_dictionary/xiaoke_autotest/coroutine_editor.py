# encoding: utf-8
import websocket
import ssl
import sys
import json
import pymysql
import threading
import queue
import time
import gevent
from gevent import monkey

# monkey.patch_all()

T_IN = 'stdin'
T_SAVE_FILE = 'save_file'
RUN_CMD = 'python socket_server.py'
threads = []
work_queue = queue.Queue()

test_db_info = {
	'db': 'kkb-smallcourse-test',
	'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
	'port': 3306,
	'user': 'ccc_test',
	'password': 'ccTsddTTdddAA123!@#'
}
prod_db_info = {
	'db': 'smallcourse',
	'host': 'rm-2zel25qqp913mff96yo.mysql.rds.aliyuncs.com',
	'port': 3306,
	'user': 'smallcourse_read',
	'password': 'RQ0mytj3IDKn'
}
test_course_id = "\'1394cb1a-96e6-4995-8d8a-ef042030b475\'"
prod_course_id = "\'1e282939-2340-4b6f-ba7e-d13250aa126a\',\'9efcc70f-b3d3-4753-a486-5aa9e6d94175\'"

def receive(ws, task_id,count = 1):
	datas = []
	#print("Receiving...")
	for i in range(0, count):
		data = ws.recv()
		if 'Error' in data:
			print('运行出错啦: task_id:{},错误信息:{}'.format(task_id, data))
		datas.append(data)
	# print(datas)
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

def on_message(ws, message):
	print('message: {}'.format(message))

def on_error(ws, error):
	print('error: {}'.format(error))

def on_close(ws):
	print("### closed ###")

def on_open(ws, file_path, code, task_id):
	#print('on_open')
	receive(ws, task_id, 2)
	send_file(ws, file_path, code)
	send_text(ws, RUN_CMD)
	receive(ws, task_id)
	send_run_remote_cmd(ws)
	res = receive(ws, task_id, 2)
	if 'Error' not in res[1]:
		print('运行通过: {}'.format(res[1]))
	# while True:
# 	# 	receive(ws,task_id, 1)

def db_connect(course_id):
	conn = pymysql.connect(**test_db_info)
	cursor = conn.cursor()
	sql = f"select id, class_id,type, props from small_task where (type='program' or type='practice') " \
		  f"and class_id in (select id from small_class where course_id in ({course_id}));"
	print(sql)
	cursor.execute(sql)
	rows = cursor.fetchmany(size=2)
	# rows = cursor.fetchall()
	return rows

def deal_data(datas):
	params = []
	for data in datas:
		param = []
		task_id, class_id, type, props = data
		try:
			save_file_path = f'{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/socket_server.py'
			url = f"wss://xiaoke-test.kaikeba.com/program/_websocket/{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1581909712371?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=N6tTtdxDwKntnkW7WAX&workspace={class_id}%2F{task_id}%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw"
			param.append(task_id)
			param.append(save_file_path)
			param.append(url)
			if props is not None:
				json_code = json.loads(props)
				if type == 'program':
					code = json_code['code']
					param.append(code)
					# print(code)
				elif type == 'practice':
					code = json_code['steps'][2]['content']
					param.append(code)
			else:
				print('props是空的:'+task_id)
			params.append(param)
		except KeyError:
			print('这是读取文件或图片的task:'+task_id)
	#把参数加入队列
	work_queue.put_nowait(params)
	return params


def socket_connect(params):
	while not work_queue.empty():
		work_queue.get_nowait()
		# print(params)
		for task_id, save_file_path, url, code in params:
			try:
				ws = websocket.create_connection(
					url,
					# print(url),
					on_error=on_error,
					on_message=on_message,
					on_close=on_close,
					sslopt={"cert_reqs": ssl.CERT_NONE}
				)
				# websocket.enableTrace(True)
				# ws = websocket.WebSocketApp(
				# 	url,
				# 	on_message=on_message,
				# 	on_error=on_error,
				# 	on_close=on_close,
				# 	sslopt={"cert_reqs": ssl.CERT_NONE}
				# )
				# ws.on_open = on_open
				# ws.run_forever()
			except Exception as error:
				print('connect error : ', error)
				sys.exit(1)
			#print("connect ok !")
			on_open(ws, save_file_path, code, task_id)
			ws.close()

if __name__ == '__main__':
	cor_list = []
	rows = db_connect(test_course_id)
	# print(rows)
	li = deal_data(rows)
	print(li)
	for x in range(3):
		time.sleep(3)
		cor = gevent.spawn(socket_connect, li)
		cor_list.append(cor)
	gevent.joinall(cor_list)


	# print(threading.enumerate())
	# while True:
	# 	print(len(threads), threading.activeCount())
		# for t in threads:
		# 	print('t:{},close: {}'.format(t.name, t.is_alive()))
		# time.sleep(5)


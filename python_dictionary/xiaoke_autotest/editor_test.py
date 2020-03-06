# encoding: utf-8
import websocket
import ssl
import sys
import json
import pymysql
import threading
import time



T_IN = 'stdin'
T_SAVE_FILE = 'save_file'
RUN_CMD = 'python socket_server.py'
threads = []
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

def receive(ws, task_id,count = 1):
	datas = []
	#print("Receiving...")
	for i in range(0, count):
		data = ws.recv()
		if 'Error' in data:
			print('运行出错啦: task_id:{},错误信息:{}'.format(task_id, data))
		datas.append(data)
		print(datas)
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
	print(send_data)
	ws.send_binary(send_data)

def on_message(ws, message):
	print('message: {}'.format(message))

def on_error(ws, error):
	print('error: {}'.format(error))

def on_close(ws):
	print("### closed ###")

def on_open(ws, file_path, code, task_id):
	#print('on_open')
	receive(ws,task_id, 2)
	send_file(ws, file_path, code)
	send_text(ws, RUN_CMD)
	receive(ws, task_id)
	send_run_remote_cmd(ws)
	res = receive(ws,task_id, 2)
	if 'Error' not in res[1]:
		print('运行通过: {}'.format(res[1]))
	# while True:
# 	# 	receive(ws,task_id, 1)

def db_connect(course_id):
	conn = pymysql.connect(**test_db_info)
	cursor = conn.cursor()
	sql = f"select id, class_id,type, props from small_task where (type='program' or type='practice') " \
		  f"and class_id in (select id from small_class where course_id in ({course_id}));"
	cursor.execute(sql)
	ids = cursor.fetchmany(size=20)
	# ids = cursor.fetchall()
	print(ids)
	return ids

def socket_connect(url, save_file_path, code,task_id):
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
	on_open(ws, save_file_path, code,task_id)
	ws.close()
	return ws

def execute_task():
	t = threading.Thread(target=socket_connect, args=(url, save_file_path, code, task_id))
	t.start()
	threads.append(t)
	print(len(threads), threading.activeCount())




if __name__ == '__main__':
	test_course_id = "\'1394cb1a-96e6-4995-8d8a-ef042030b475\'"
	prod_course_id = "\'1e282939-2340-4b6f-ba7e-d13250aa126a\',\'9efcc70f-b3d3-4753-a486-5aa9e6d94175\'"
	task_ids = []
	used_usls =[]
	ids = db_connect(test_course_id)
	for task_id, class_id, type, props in ids:
		save_file_path = f'{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/socket_server.py'
		url = f"wss://xiaoke-test.kaikeba.com/program/_websocket/{class_id}/{task_id}/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1581909712372?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=N6tTtdxDwKntnkW7WAX&workspace={class_id}%2F{task_id}%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw"
		json_code = json.loads(props)
		if type == 'program':
			code = json_code['code']
		elif type == 'practice':
			code = json_code['steps'][2]['content']
		#print(code)
		time.sleep(5)
		execute_task()


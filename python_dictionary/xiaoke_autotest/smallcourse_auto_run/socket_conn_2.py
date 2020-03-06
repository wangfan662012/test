# encoding: utf-8
import websocket
import ssl
import json
from get_db_data import db_connect, deal_data
import threading
import time
try:
	import thread
except ImportError:
	import _thread as thread


RUN_CMD = 'python socket_server.py'
end_symbol = '["stdout", "$"]'
run_symbol = '["stdout", "python socket_server.py"]'
run_symbol2 = r'["stdout", "python socket_server.py\r\n"]'
total_error = []

def socket_connect():
	websocket.enableTrace(True)  # 打开跟踪，查看日志
	ws = websocket.WebSocketApp(
		url,
		on_message=on_message,
		on_error=on_error,
		on_close=on_close,
	)
	ws.on_open = on_open
	ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
	return ws

def on_message(ws, message):
	messages.append(message)
	print('message:'+message)
	if end_symbol in messages:
		if messages.count(end_symbol) == 1 and messages[-1] == end_symbol:
			send_msg(ws, file_path, code)
		elif messages.count(end_symbol) == 2:
			ws.close()
			print('运行完美结束')
	if run_symbol in messages and messages[-3] == run_symbol:
		if 'Error' not in message:
			ws.close()
			print('运行结果无异常, 关闭连接.......')
		else:
			print('运行出错啦, task_id:{},error: {}'.format(task_id, message))
	if run_symbol2 in messages and messages[-2] == run_symbol2:
		if 'Error' not in message:
			ws.close()
			print('运行结果无异常, 关闭连接.......')
		else:
			print('运行出错啦, task_id:{},error: {}'.format(task_id, message))

def on_error(ws, error):
	print('运行出错啦, task_id:{},error: {}'.format(task_id, error))
	errors = [time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), task_id, error]
	total_error.append(errors)

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	def run(*args):
		print("连接成功.........")
	thread.start_new_thread(run, ())
	# threading.Thread(target=run).start()

def send_msg(ws, path, content):
	send_file = ['save_file', path, content]
	send_text = ['stdin', RUN_CMD]
	send_run_cmd = ['stdin', '\r']
	datas = [send_file, send_text, send_run_cmd]
	for data in datas:
		send_data = json.dumps(data)
		# print('sending ... '+send_data)
		ws.send(send_data)

def write_error(allerror):
	print('----------错误信息写入文件---------------')
	file = open('./error_file.txt', 'w+')
	for e in allerror:
		file.write(str(e)+'\n')
	print('----------写入完成---------------')


if __name__ == '__main__':
	rows = db_connect()
	print('数据库查询结果:{}'.format(rows))
	li = deal_data(rows)
	print('处理后的数据(task_id,save_file_path,url,code):{}'.format(li))
	
	for task_id, file_path, url, code in li:
		# print('task_id:{},file_path{},url:{},code{}'.format(task_id, file_path, url, code))
		messages = []
		ws = socket_connect()

	write_error(total_error)

	# task_id = '8f99a83a-4bb6-4a34-a302-262b070fe31e'
	# file_path = 'd8f87db2-c07e-4cb6-aaf0-aea42770c4c6/8f99a83a-4bb6-4a34-a302-262b070fe31e/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/socket_server.py'
	# url = 'wss://xiaoke-test.kaikeba.com/program/_websocket/d8f87db2-c07e-4cb6-aaf0-aea42770c4c6/8f99a83a-4bb6-4a34-a302-262b070fe31e/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1582782848283?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=06MgP1QeJbqxt1dWPfT&workspace=d8f87db2-c07e-4cb6-aaf0-aea42770c4c6%2F8f99a83a-4bb6-4a34-a302-262b070fe31e%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw'
	# code = "def rounding(num):\n    if num%1==0:\n        return int(num)\n    else:\n    \tdata = int(num)+1\n    \treturn data\nnum=float(input('请输入数字：'))\nnum1 = rounding(num)\nprint(num1)"
	#
	# data = ["save_file","d8f87db2-c07e-4cb6-aaf0-aea42770c4c6/8f99a83a-4bb6-4a34-a302-262b070fe31e/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/socket_server.py","def rounding(num):\n    if num%1==0:\n        return int(num)\n    else:\n    \tdata = int(num)+1\n    \treturn data\nnum=float(input('请输入数字：'))\nnum1 = rounding(num)\nprint(num1)"]
	# ws = socket_connect()
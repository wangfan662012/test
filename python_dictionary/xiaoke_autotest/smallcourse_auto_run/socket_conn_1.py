# # encoding: utf-8
# import websocket
# import ssl
# import sys
# import json
# from get_db_data import db_connect, deal_data
# import threading
# import queue
# import time
# import gevent
# from gevent import monkey
#
# monkey.patch_all()
#
# RUN_CMD = 'python socket_server.py'
# threads = []
# work_queue = queue.Queue()
#
# rows = db_connect()
# print('数据库查询结果:{}'.format(rows))
# li = deal_data(rows)
# print('处理后的数据(task_id,save_file_path,url,code):{}'.format(li))
# # 把参数加入队列
# work_queue.put_nowait(li)
#
# def socket_connect(params):
# 	while not work_queue.empty():
# 		work_queue.get_nowait()
# 		# print(params)
# 		for task_id, save_file_path, url, code in params:
# 			try:
# 				ws = websocket.create_connection(
# 					url,
# 					# print(url),
# 					sslopt={"cert_reqs": ssl.CERT_NONE}
# 				)
# 				# websocket.enableTrace(True)
# 				# ws = websocket.WebSocketApp(
# 				# 	url,
# 				# 	on_message=on_message,
# 				# 	on_error=on_error,
# 				# 	on_close=on_close,
# 				# 	sslopt={"cert_reqs": ssl.CERT_NONE}
# 				# )
# 				# ws.on_open = on_open
# 				# ws.run_forever()
# 			except Exception as error:
# 				print('connect error : ', error)
# 				sys.exit(1)
# 			#print("connect ok !")
# 			on_open(ws, save_file_path, code, task_id)
# 			ws.close()
#
# def receive(ws, task_id,count = 1):
# 	datas = []
# 	#print("Receiving...")
# 	for i in range(0, count):
# 		data = ws.recv()
# 		if 'Error' in data:
# 			print('运行出错啦: task_id:{},错误信息:{}'.format(task_id, data))
# 		datas.append(data)
# 	print(datas)
# 	return datas
#
# def send_run_cmd(ws):
# 	send(ws, ['stdin', '\r'])
#
# def send_file(ws, path, content):
# 	msg = ['save_file', path, content]
# 	send(ws, msg)
#
# def send_text(ws, text):
# 	msg = ['stdin', text]
# 	send(ws, msg)
#
#
# def send(ws, data: list):
# 	send_data = json.dumps(data)
# 	#print('sending ... ')
# 	print(send_data)
# 	ws.send_binary(send_data)
#
# def on_message(ws, message):
# 	print('message: {}'.format(message))
#
# def on_error(ws, error):
# 	print('error: {}'.format(error))
#
# def on_close(ws):
# 	print("### closed ###")
#
# def on_open(ws, file_path, code, task_id):
# 	#print('on_open')
# 	receive(ws, task_id, 2)
# 	send_file(ws, file_path, code)
# 	send_text(ws, RUN_CMD)
# 	receive(ws, task_id)
# 	send_run_cmd(ws)
# 	res = receive(ws, task_id, 2)
# 	if 'Error' not in res[1]:
# 		print('运行通过: {}'.format(res[1]))
# 	# while True:
# # 	# 	receive(ws,task_id, 1)
#
#
#
#
# if __name__ == '__main__':
# 	socket_connect(li)
# 	# cor_list = []
# 	# for x in range(3):
# 	# 	time.sleep(3)
# 	# 	cor = gevent.spawn(socket_connect, li)
# 	# 	cor_list.append(cor)
# 	# gevent.joinall(cor_list)
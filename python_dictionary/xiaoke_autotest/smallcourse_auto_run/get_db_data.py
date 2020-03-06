# encoding: utf-8
import json
import pymysql
import configparser

# 读取配置
con = configparser.ConfigParser()
con.read('config.ini', encoding='utf-8')
items = con.items('test_config')    #取测试/生成配置
config_info = dict(items)

course_id = config_info['course_id']
db_info = eval(config_info['db_info'])
union_id = config_info['union_id']
token = config_info['token']
run_count = int(config_info['run_count'])
hostname = config_info['hostname']

def db_connect():
	conn = pymysql.connect(**db_info)
	cursor = conn.cursor()
	sql = f"select id, class_id,type, props from small_task where (type='program' or type='practice') " \
		  f"and class_id in (select id from small_class where course_id in ({course_id}));"
	print('执行的sql:{}'.format(sql))
	cursor.execute(sql)
	if not run_count == -1:
		rows = cursor.fetchmany(size=run_count)
	else:
		rows = cursor.fetchall()
	return rows

def deal_data(rows):
	params = []
	for data in rows:
		task_id, class_id, type, props = data
		try:
			save_file_path = f'{class_id}/{task_id}/{union_id}/socket_server.py'
			url = f"wss://{hostname}/program/_websocket/{class_id}/{task_id}/{union_id}/1581909712371?user_id={union_id}&token={token}&workspace={class_id}%2F{task_id}%2F{union_id}"
			if props is not None:
				json_code = json.loads(props)
				if type == 'program':
					code = json_code['code']
					param = [task_id, save_file_path, url, code]
					# print(code)
				elif type == 'practice':
					code = json_code['steps'][2]['content']
					param = [task_id, save_file_path, url, code]
			else:
				print('props是空的, taskid:'+task_id)
			params.append(param)
		except KeyError:
			print('这是读取文件或图片的task, taskid:'+task_id)
	return params



if __name__ == '__main__':
	rows = db_connect()
	print('数据库查询结果:{}'.format(rows))
	li = deal_data(rows)
	print('处理后的数据(task_id,save_file_path,url,code):{}'.format(li))



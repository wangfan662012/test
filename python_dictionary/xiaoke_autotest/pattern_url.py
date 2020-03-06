# encoding: utf-8
import json
import pymysql
import queue
import time
import re

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


def db_connect(course_id):
	conn = pymysql.connect(**prod_db_info)
	cursor = conn.cursor()
	sql = f"select id, class_id,type, props from small_task where (type='program' or type='practice') " \
		f"and class_id in (select id from small_class where course_id in ({course_id}));"
	cursor.execute(sql)
	# ids = cursor.fetchmany(size=50)
	ids = cursor.fetchall()
	print(ids)
	return ids

if __name__=='__main__':
	test_course_id = "\'1394cb1a-96e6-4995-8d8a-ef042030b475\'"
	prod_course_id = "\'1e282939-2340-4b6f-ba7e-d13250aa126a\',\'9efcc70f-b3d3-4753-a486-5aa9e6d94175\'"
	param = []
	params = []
	cor_list = []
	used_urls = []
	
	ids = db_connect(prod_course_id)
	for task_id, class_id, type, props in ids:
		try:
			pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式
			used_url = re.findall(pattern, props)
			used_urls.append(used_url)
		except TypeError:
			print('类型错误:'+task_id)
	print(used_urls)




# print(threading.enumerate())
# while True:
# 	print(len(threads), threading.activeCount())
# for t in threads:
# 	print('t:{},close: {}'.format(t.name, t.is_alive()))
# time.sleep(5)


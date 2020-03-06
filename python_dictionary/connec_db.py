import pymysql

dbtest = {
'user':'ccc_test',
'password':'ccTsddTTdddAA123!@#',
'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
'port': 3306,
'db':'kkb-smallcourse-test',
'charset':'utf8'
}
sql = "select * from small_course limit 1;"

def select_db(cur):
	cur.execute(sql)
	data = cur.fetchone()
	return data


conn = pymysql.connect(**dbtest)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
print(select_db(cursor))
cursor.close()

# import pymysql
#
# conn = pymysql.connect(host='rm-bp18pciktjjurinnvo.mysql.rds.aliyuncs.com', port=3306, user='smallcourse',
# 	passwd='3E1d9m3MIj7e', db='kkb-smallcourse-test', charset='utf8')
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# def get_data(sql):
# 	cursor.execute(sql)
# 	# conn.commit()
# 	data = cursor.fetchmany(5)
# 	return data

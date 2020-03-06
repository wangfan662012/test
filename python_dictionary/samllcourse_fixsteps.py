import mysql.connector
import json

dbTest = {
  'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
  'user': 'ccc_test',
  'password': 'ccTsddTTdddAA123!@#',
  'database': 'kkb-smallcourse-test',
  'charset': 'utf8'
}

courseIdTest = '1394cb1a-96e6-4995-8d8a-ef042030b475'

dbProduct = {
  'host': 'rm-2zel25qqp913mff96yo.mysql.rds.aliyuncs.com',
  'user': 'yuyingtao',
  'password': '',
  'database': 'smallcourse',
  'charset': 'utf8'
}

courseId = courseIdTest
dbConfig = dbTest

mydb = mysql.connector.connect(**dbConfig)
mycursor = mydb.cursor(dictionary=True)

mycursor.execute('SELECT id, type FROM small_class where course_id = %s', (courseId,))

def addTagForContent(content):
  content = content.replace('\n', '<br>')
  ret = '<p>' + content + '</p>'
  return ret

def fixClassProps(row, cur):
  if row['type'] != 'exercises' and row['type'] != 'practice':
    return

  classId = row['id']
  cur.execute('SELECT id, props from small_task where class_id = %s limit 0, 1', (classId,))
  taskRow = cur.fetchone()
  propJson = json.loads(taskRow['props'])

  if 'description' not in propJson or 'steps' not in propJson:
    print('此 task 没有 description steps', taskRow['id'])
    return

  descriptionArray = propJson['description']
  stepsArray = propJson['steps']

  for desc in descriptionArray:
    # print('desc', desc)
    if desc['title'] == '题目要求':
      stepsArray[0]['content'] = addTagForContent(desc['content'])
    elif desc['title'] == '题目讲解':
      stepsArray[1]['content'] = addTagForContent(desc['content'])
    elif desc['title'] == '书写代码':
      stepsArray[2]['content'] = desc['content']

  cur.execute('UPDATE small_task SET props = %s WHERE id = %s', (json.dumps(propJson, ensure_ascii=False), taskRow['id']))

for x in mycursor.fetchall():
    fixClassProps(x, mycursor)

mydb.commit()

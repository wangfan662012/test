import mysql.connector
import json

dbTest = {
  'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
  'user': 'ccc_test',
  'password': 'ccTsddTTdddAA123!@#',
  'database': 'kkb-smallcourse-test'
}
# 爬虫课 b33532e3-664b-4139-83da-0e341fa38eb3
# 基础课 aa5c452b-4d34-4822-97c7-9123fbe96b8b
courseMapTest = {
  'source': 'cc512363-8de5-4ea3-af93-13310f035a20',
  'target': '1394cb1a-96e6-4995-8d8a-ef042030b475'
}

dbProduct = {
  'host': 'kuick-test1-o.mysql.rds.aliyuncs.com',
  'user': 'ccc_test',
  'password': 'ccTsddTTdddAA123!@#',
  'database': 'kkb-smallcourse-test'
}

courseMapProd = {
  'source': '5b9fc092-ce12-4bf6-b29c-6007bd0c87d7',
  'target': 'e403f2cb-5bdf-436b-9435-a4a9502f2fee'
}

# 根据不同环境设置不同变量
dbConfig = dbTest
courseMap = courseMapTest

def createClassList(cursorId, cur):
  print('courseId', cursorId)
  cur.execute('SELECT id, first_class_id from small_course where id = %s', (cursorId,))
  row = cur.fetchone()
  firstClassId = row['first_class_id']
  cur.execute('SELECT id, next_class_id FROM small_class where course_id = %s', (cursorId,))

  classDict = {}
  for x in cur:
    classDict[x['id']] = x['next_class_id']

  classList = []
  classId = firstClassId
  while (classId is not None and classId != ''):
    nextId = classDict[classId]
    classList.append(classId)
    classId = nextId

  return classList

mydb = mysql.connector.connect(**dbConfig)
mycursor = mydb.cursor(dictionary=True)

# 获取 class 列表
sourceClassList = createClassList(courseMap['source'], mycursor)
print('sourceClassList', sourceClassList)

targetClassList = createClassList(courseMap['target'], mycursor)
print('targetClassList', targetClassList)

if (len(sourceClassList) != len(targetClassList)):
  print('size of sourceClassList', len(sourceClassList))
  print('size of targetClassList', len(targetClassList))
  raise AssertionError('课程数量不匹配')

classMap = []

for i in range(len(targetClassList)):
  classMap.append({
    'source': sourceClassList[i],
    'target': targetClassList[i]
  })

print('class Map', classMap)
exit


## 根据 classId 
for classPair in classMap:
  sourceJson = {}
  targetJson = {}

  sourceId = ''
  targetId = ''

  # soruce class
  mycursor.execute('SELECT id, type, props from small_task where class_id = %s limit 0, 1', (classPair['source'],))
  row = mycursor.fetchone()
  sourceId = row['id']
  propJson = json.loads(row['props'])
  sourceJson = propJson

  if row['type'] != 'exercise' and row['type'] != 'practice':
    continue

  # target class
  mycursor.execute('SELECT id, props from small_task where class_id = %s limit 0, 1', (classPair['target'],))
  row = mycursor.fetchone()
  targetId = row['id']
  propJson = json.loads(row['props'])
  targetJson = propJson
  
  if ('knowledgeReview' in sourceJson):
    targetJson['knowledgeReview'] = sourceJson['knowledgeReview']

  if ('steps' in sourceJson):
    targetJson['steps'] = sourceJson['steps']

  mycursor.execute('UPDATE small_task SET props = %s WHERE id = %s', (json.dumps(targetJson), targetId))
  mydb.commit()

  print(sourceId, targetId)

mydb.close()

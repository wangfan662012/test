import configparser

file = 'config.ini'

# 创建配置文件对象
con = configparser.ConfigParser()

# 读取文件
con.read(file, encoding='utf-8')

# 获取所有section
sections = con.sections()
print(sections)

# 获取特定section
items = con.items('test_db_config')

# 可以通过dict方法转换为字典
items = dict(items)

print(items)

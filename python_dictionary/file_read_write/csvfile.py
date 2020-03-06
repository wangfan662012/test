import csv

# 需要写入的数据
score1 = ['math', 95]
score2 = ['english', 90]

# 打开文件，追加a, newline=""，可以删掉行与行之间的空格
file = open("score.csv", "w", newline="")

# 设定写入模式
csv_write = csv.writer(file)

# 写入具体内容
csv_write.writerow(score1)
csv_write.writerow(score2)
file.close()

# idfile = open('id.csv', 'r', newline='')
# csv_reader = csv.reader(idfile)
# for row in csv_reader:
# 	print(row)



# 打开csv文件
file1 = open("score.csv")
# 读取文件内容，构造csv.reader对象
reader = csv.reader(file1)

# 打印reader中的内容
for item in reader:
    print(item)
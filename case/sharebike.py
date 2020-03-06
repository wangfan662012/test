class Bike:
	def __init__(self, NO, age, state=0):
		self.NO = NO
		self.age = age
		self.state = state

	def __str__(self):
		if self.state ==0:
			status = '待租借'
		elif self.state ==1:
			status = '已租借'
		return '车辆编号:%s,已运营 %d 年,车辆状态:%s'% (self.NO, self.age, status)

class Manage:
	bike_list = []
	def __init__(self):
		bike1 = Bike('0012', 3)
		bike2 = Bike('0056',1)
		self.bike_list.append(bike1)
		self.bike_list.append(bike2)

	def menu(self):
		print('欢迎使用共享单车租赁系统! \n')
		while True:
			num = int(input('请选择服务项目: 1.查询车辆信息 2.共享车辆 3.租借车辆 4.归还车辆 5.退出系统 \n'))
			if num == 1:
				self.info_bike()
			elif num == 2:
				self.add_bike()
			elif num == 3:
				self.lease_bike()
			elif num == 4:
				self.revert_bike()
			elif num == 5:
				print('欢迎再次使用!')
				break

	def info_bike(self):
		for i in self.bike_list:
			print(i)

	def add_bike(self):
		new_No = input('请输入车辆编码:')
		new_age = int(input('请输入车辆年限:'))
		new_bike = Bike(new_No, new_age)
		self.bike_list.append(new_bike)
		print('共享车辆成功')

	def lease_bike(self):
		lease_No = input('请输入要租赁的车辆编号:')
		bike = self.select_bike(lease_No)
		if bike != None:
			if bike.state == 0:
				print('你可以骑走啦')
				bike.state = 1
			else:
				print('这辆车被借走啦')
		else:
			print('这辆车不存在')


	def revert_bike(self):
		revert_NO = input('请输入车辆编号:')
		bike = self.select_bike(revert_NO)
		if bike != None:
			if bike.state ==1:
				print('车辆归还成功!')
				bike.state = 0
			else:
				print('车辆还未租赁噢')
		else:
			print('亲,这不是我家的车噢')

	def select_bike(self, NO ):
		for bike in self.bike_list:
			if bike.NO == NO:
				return bike
b = Manage()
b.menu()
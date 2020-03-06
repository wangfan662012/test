import requests

count = 100
res = requests.get('https://deal-admin.kuick.cn/api/v1.7/app/2414aaa7-22eb-4378-bc30-789627ad255d/member/4808/customers'
				   f'?customer_group_id=all&start_index=0&count={count}&access_token=96db6d0945e011d56c101d53d71661080d5081e8'
				   '398af5588fa5f2b2b8d2ffc28ce359018e3d47b6d29ae4a51960e9ce66dd78306065c58f33e06a4d7170adf7&app_secret='
				   'bb1549b9-4981-4b38-a9a8-d4b95cb69427&https=1')
li = res.json()['data']
print(len(li))

customerIds = []
for i in li:
	customerId = i['id']
	value = ''
	customerIds.append(customerId)
	upd_url = f'https://deal-admin.kuick.cn/api/v1.7/app/2414aaa7-22eb-4378-bc30-789627ad255d/member/4808/customer/{customerId}?access_token=96db6d0945e011d56c101d53d71661080d5081e8398af5588fa5f2b2b8d2ffc28ce359018e3d47b6d29ae4a51960e9ce66dd78306065c58f33e06a4d7170adf7&app_secret=bb1549b9-4981-4b38-a9a8-d4b95cb69427&https=1'
	body = {"name": "Fake0yHrbU", "title": "", "email": "", "phone": "", "company": "", "sex": "0", "province": "", "city": "",
	 "county": "", "address": "", "age_state": "0", "kuickUserId": 4808, "lead_source": "", "grade": 0, "industry": "",
	 "intentionality": "0", "from": "create_fake_customer", "create_way": 0, "is_officialaccount_fans": 0,
	 "gudakeng": f"{value}", "id": f"{customerId}"}
	result = requests.put(url=upd_url, json=body, headers={'Content-Type': 'application/json'})
	print(result)
print(customerIds)
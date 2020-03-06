import re

def huiwen(str):
	result = ''.join(re.findall(r'[A-Za-z0-9]', str)).lower()

	# if len(result) <= 1:
	# 	return True
	# else:
	# 	for i in range((len(result)//2)):
	# 		if result[i] == result[-i-1]:
	# 			if i == (len(result)//2 - 1) and result[i] == result[-i-1]:
	# 				return True
	# 		else:
	# 			return False

	if len(result) <= 1:
		return True
	else:
		i = 0
		j = len(result)-1
		while i < j:
			if result[i] == result[j]:
				i += 1
				j -= 1
				if i >= j:
					return True
			else:
				return False


#str = 'A man, @a plan,# a c dca你好nal: Panama'
str='  aba'
print(huiwen(str))
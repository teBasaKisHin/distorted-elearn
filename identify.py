def suc(text):
	import re
	if re.search(r"ログインしています",text):
		print("ログインしました")
	else:
		print("失敗しました")

def sessGet(text):
	import re
	s = re.split(r'\"sesskey\":',text)[1]
	s = re.split(r'\"',s)[1]
	return s


def suc(text):
	import re
	if re.search(r"ログインしています",text):
		pass
	else:
		print("failed")

def sessGet(text):
	import re
	s = re.split(r'\"sesskey\":',text)[1]
	s = re.split(r'\"',s)[1]
	return s


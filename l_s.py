def suc(text):
	import re
	if re.search(r"ログインしています",text):
		print("ログインしました")
	else:
		print("失敗")


	

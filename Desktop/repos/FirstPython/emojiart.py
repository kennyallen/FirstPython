# emoji = "\U0001f600"
# spaced_emo = emoji + " "
# for rows in range(11):
# 	print(spaced_emo * rows)
spaced_emo = "\U0001f600" + " "
rows = 0
while rows < 11:
	rows = rows + 1
	print(spaced_emo * rows)
days = {"Sunday":0,"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}
months = {"january":0, "february":3 ,"march": 3, "april":6, "may":1 ,"june":4 ,"july":6 ,"august":2 ,"september":5 ,"october":0, "november":3, "december":5}
year = {}
for i in range(1600,1699):
	year[i] = 6
for j in range(1700,1799):
	year[j] = 4
for k in range(1800,1899):
	year[k] = 2
for l in range(1900,1999):
	year[l] = 0
for m in range(2000,2099):
	year[m] = 6

print("This is an Automatic Day Finder Machine !!")
dd = int(input("Enter the date : "))
mm = input("Enter the month : ").lower()
for i in months:
	if i == mm:
		m = months[i]
yy = int(input("Enter the year : "))
for k in year:
	if k == yy:
		y = year[k]
p = (yy % 100)
p += p // 4 + dd + m + y
index = p % 7

for key, val in days.items():
	if val == index:
		result= key

print(f"The Day of Date {dd}{mm}{yy} is {result}")
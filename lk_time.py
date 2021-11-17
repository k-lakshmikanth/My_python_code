import time

z=time.ctime()
lk=list(z.split(" "))

def my_time():
	kk=list(lk[3].split(":"))
	if int(kk[0])>12:
		print(int(kk[0])-12,":",kk[1],"PM")
	else:
		print(kk[0],":",kk[1],"AM")
		
def my_day():
	vk=lk[0]
	print(vk)

def my_date():
	pk=lk[2]+"-"+lk[1]+"-"+lk[4]
	print(pk)
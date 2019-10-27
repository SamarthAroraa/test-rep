def binary_con(n,res):
	n=int(n)
	res=str(res)
	if n>1:
		binary_con(n/2)
	res=res+str(n%2)


t=int(input())
while(t-=1):
	n=input()
	res=''
	binary_con(n,res)
	print(res)

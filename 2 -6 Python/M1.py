# M1.p

print("inside Module M1.py name is : {}".format(__name__));

if __name__=='__main__':
	#do the which is done when it is directly called
	print("hello guys kese hai app log: mera naam hai : {}".format(__name__));
else:
	# do the work which is done when it is imported as Module
	print("we are in else block");
def GetFileNamesInFolder(dir):
	from os import listdir
	return listdir(dir)

def CheckTypo(line):
	ac=line.split(':')
	if len(ac)>1 and ac[-1].find("N")>-1:
		return True
	return False

def LocateTypo(filename):
	errorlines=[]
	count=0
	f=open(filename)
	for line in f:
		if CheckTypo(line): errorlines.append(count)
		count+=1
	return errorlines

def FixTypo(dir,filename,linenumber):
	from os import close,remove
	from shutil import move
	f=open(dir+'/'+filename)
	fnew=open(dir+'/temp','w')
	count=0
	for line in f:
		if count==linenumber:
			newline=line.replace("N","M")
			#print newline
			fnew.write(newline)
		else:
			fnew.write(line)
		count+=1
	fnew.close()
	remove(dir+'/'+filename)
	move(dir+'/temp',dir+'/'+filename)
	return
	
def main():
	dir='../../PyTrieste/shellExample/cleaneddata'
	filenames=GetFileNamesInFolder(dir)
	for filename in filenames:
		errorlines=LocateTypo(dir+'/'+filename)
		if len(errorlines)>0:
			#print filename
			#print errorlines
			for linenum in errorlines: FixTypo(dir,filename,linenum)

main()

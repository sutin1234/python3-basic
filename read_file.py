def readFile(file_path):
	f = open(file_path, 'r')
	contents = f.read()
	f.close()
	return contents

def writeFile(file_path, contents):
	f = open(file_path, 'w+')
	f.write(contents)
	f.close()
	return f

if __name__ == '__main__':
	file = readFile('docs/read.txt')
	writeFile('docs/write.txt', file);
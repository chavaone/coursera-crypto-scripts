

from Crypto.Hash import SHA256

filename = "video1.mp4"


ha = SHA256.new()

f = open(filename)
file = f.read()
blocks = [(1024*i,1024*(i+1)) for i in range(len(file)/1024)]

if len(file):
	blocks = blocks + [(blocks[-1][0]+1024,len(file))]

h = ""
for i in range(len(blocks)-1,-1,-1):
	ha = SHA256.new()
	ha.update(file[blocks[i][0]:blocks[i][1]] + h)
	h = ha.digest()


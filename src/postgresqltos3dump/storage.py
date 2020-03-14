def local(infile, outfile):  #1
	outfile.write(infile.read())  #1
	outfile.close()  #1
	infile.close()  #1

def s3(client, infile, bucket, filename): #3
	client.upload_fileobj(infile, bucket, filename) #4
	#pass #3

#1 PASS	
#3 AssertionError: Expected call: upload_fileobj(<_io.BufferedRandom name=10>, 'bucket', 'file-name')

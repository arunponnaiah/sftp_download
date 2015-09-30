import pysftp

#def printTotals(transferred, toBeTransferred):
#    print "Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred)

with  pysftp.Connection(host="10.5.69.209", username="komuser",password="Komu53R@") as sftp:
        with sftp.cd('sandvine'):
	 with open("input.txt", "r") as file:
	   data = file.readlines()
           for line in data:
		print 'downloading ' , line.strip()
		#sftp.get(line.strip(),callback=printTotals)
		sftp.get(line.strip())
	 file.close()

#!/usr/bin/python
import pysftp
import sys

#def printTotals(transferred, toBeTransferred):
#    print "Transferred: {0}\tOut of: {1}".format(transferred, toBeTransferred)
cmdargs = str(sys.argv)	
print cmdargs
hostname = sys.argv[1]
user=sys.argv[2]
passwd=sys.argv[3]
remotedir=sys.argv[4]
localdir=sys.argv[5]

with  pysftp.Connection(host=hostname, username=user,password=passwd) as sftp:
 print 'downloading from ' , remotedir
 sftp.get_d(remotedir,localdir)

# memo.py
import sys
import time
def usage():
    print """   
Usage
=====

%s -v : View memo
%s -a : Add memo
""" % (sys.argv[0], sys.argv[0])
if not sys.argv[1:] or sys.argv[1] not in ['-v', '-a']:
    usage()
elif sys.argv[1] == '-v':
    try: print open("memo.txt").read()
    except IOError: print "memo does not exist!"
elif sys.argv[1] == '-a':
    word = raw_input("Enter memo: ")
    f = open("memo.txt", 'a')
    f.write(time.ctime() + ': ' + word+'\n')
    f.close()
    print "Added"

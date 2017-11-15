#!/usr/bin/python3
import argparse
import os
from pprint import pprint
import random

parser=argparse.ArgumentParser(description="Select a random file from any number of given directories")
parser.add_argument('dirs',nargs="*",help="list of directories to search in",default=['.'])
parser.add_argument('-f',action='store_true',help="If this flag is present, use naive file selection.\nThe file will be chosen out of the total pool of files instead of giving equal weight to each directory")
parser.add_argument('-n',action='store_true',help='if this flag is present, do not recurse')

args=parser.parse_args()

#print(args.dirs)

files=('',[],[])
#this big bock will just determine the set of files we choose from
if args.n:
	dirs=[x for x in args.dirs if os.path.isdir(x)]
	path=random.choice(dirs)
	files=(path,[],[f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))])
else:
	dirs=[]
	for path in args.dirs:
		dirs+=[x for x in os.walk(path) if x and len(x[2])]

	if args.f:
		f=[]
		for d in dirs:
			f+=[os.path.join(d[0],x) for x in d[2]]
		print(random.choice(f))
		exit(0)
	
	files=random.choice(dirs)

	#pprint(dirs)

#pprint(files)

print(os.path.join(files[0],random.choice(files[2])))

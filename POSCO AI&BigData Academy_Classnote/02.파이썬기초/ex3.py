import sys
args = sys.argv[1:3]
print(args)
f = open(args[0],'r')
with open(args[1],'w') as f_copy:
    f_copy.write(f.read())
f.close()
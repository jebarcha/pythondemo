import sys

# extend app.py -a -b -c

# print(sys.argv) # ['15-command-line-args.py', '-a', '-b', '-c']

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

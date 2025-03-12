import sys

if len(sys.argv) == 2 :
    string = sys.argv[1]
    count = string.count('z')
    if count > 0 :
        for _ in range(count):
            print("z")
            
    else:
        print("none")
    
else:
    print("none")
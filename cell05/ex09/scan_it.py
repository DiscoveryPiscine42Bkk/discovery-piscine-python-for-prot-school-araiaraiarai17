import sys

if len(sys.argv) == 3 :
    scan = sys.argv[1]
    it = sys.argv[2]
    count = it.count(scan)
    
    if count > 0 :
        print(count)
    
    else:
        print("none")
        
else:
    print("none")
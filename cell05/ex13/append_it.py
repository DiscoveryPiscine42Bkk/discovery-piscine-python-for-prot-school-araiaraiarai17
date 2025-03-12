import sys

if len(sys.argv) > 1:
    for para in sys.argv[1:]:
        if not para.endswith('ism'):
            print(para + 'ism')
            
else:
    print("none")
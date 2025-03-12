import sys

def downcase_it(text):
    return text.lower()

def main():
    if len(sys.argv) == 1 :
        print("none")
        
    else:
        for para in sys.argv[1:]:
            print(downcase_it(para))
            
if __name__ == "__main__" :
    main()
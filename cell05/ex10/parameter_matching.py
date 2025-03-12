def parametmat(paramaet_w,t,o) :
    if num_paramet != 1 :
        print("none")
    
    else:
        
        word = input("What was the parameter? : ")
        if word == paramaet_w :
            print("Good job!")
            
        else:
            print("Nope sorry...")
num_paramet = parametmat.__code__.co_argcount

parametmat('Hello','k','meow')
    
def greet(name = "noble stranger") :
    if not isinstance(name, str):
        print("Error! It was not a name.")
        
    else:
        print("Hello, ", name)
        
greet("A")
greet("V")
greet("noble stranger")
greet(123)
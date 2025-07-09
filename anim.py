import time
 
st = [
    "I am Soumalya Ghosh",
    "I love coding",
    "This is my implementation of a typewriter effect",
    "Written in Python"
    ]
  
def animate(string:str):
    l = ["|","/","-","\\"]
    time.sleep(0.1)
    print("\r" + " "*(len(string)+1), end="")
    for i in range(len(string)):
        time.sleep(0.1)
        print(f'\r{l[i%4]} {string[0:i+1]}' + " "*(len(string)-i), end="")
    time.sleep(1)
    for i in reversed(range(len(string))):
        time.sleep(0.05)
        print(f'\r{l[i%4]} {string[0:i]}' + " "*(len(string)-i+1),end="")
                                                                      
def animate_list(l:list):
    for i in l:
        animate(i)
    animate_list(l)
            
animate_list(st)
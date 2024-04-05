import threading

shared_var=0
def count():
    global shared_var
    for i in range(10000):
        for j in range(10000):
            shared_var+=1
            
thread1=threading.Thread(target=count)
thread2=threading.Thread(target=count)

thread1.start()
thread2.start()

while (thread1.is_alive()) and (thread2.is_alive()):
    pass
print(shared_var)
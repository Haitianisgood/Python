import thread
def run(n):
 for i in range(n):
    print i
    
    
thread.start_new_thread(run,(4,))
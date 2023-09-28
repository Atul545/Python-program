import time
from plyer import notification

if __name__ =="__main__":
    notification.notify(
        title="***Please Drink water***",
        message='''Water is necessary for the organisms to maintain 
a distinct level of water within their bodies in order to stay alive.''',
         
        timeout=1  
    )
    time.sleep(6)
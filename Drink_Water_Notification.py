from plyer import notification
import time

if __name__=='__main__':
   while True:
       notification.notify(
          title="**take Rest**",
          message="for better helth",
          timeout=10)
       time.sleep(30)


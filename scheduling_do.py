from threading import Timer
import dataload

curl1 = "https://api.thingspeak.com/channels/332251/feeds.json?api_key=LIUIIAXK0HICC7OA&results=2"
curl2 = "https://api.thingspeak.com/channels/332335/feeds.json?api_key=O81NGSHFYAASSUFP&results=2"

#!/usr/bin/python3

class RepeatedTimer(Timer):
  def __init__(self, interval, function, args=[], kwargs={}):
    Timer.__init__(self, interval, self.run, args, kwargs)
    self.thread = None
    self.function = function

  def run(self):
    self.thread = Timer(self.interval, self.run)
    self.thread.start()
    self.function(*self.args, **self.kwargs)

  def cancel(self):
    if self.thread is not None:
      self.thread.cancel()
      self.thread.join()
      del self.thread

if __name__=='__main__':

  import time

  def main():
    main.counter += 1
    dataload.data_load(curl1,1)
    dataload.data_load(curl2,2)
  main.counter = 0

  t = RepeatedTimer(60, main)
  t.start()
  time.sleep(3000)
  t.cancel()
  print("Done.")

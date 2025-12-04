import time

### Function to print timestamped messages
startingtime = time.time()


def tsprint(message):
  timestamp = time.time() - startingtime
  print(f"[{timestamp:.4f}] {message}")


def ttime():
  timestamp = time.time() - startingtime
  return timestamp

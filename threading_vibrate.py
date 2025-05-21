import time, threading, requests, os

t=1

nV = requests.get("https://tknight5.github.io/action").text
nV = int(nV.strip("\n"))

threads=[]

for i in range(nV):
	thread = threading.Thread(name=f"thread_{i}", target=lambda: os.system("echo vibrate"))
	thread.start()
	threads.append(thread)
	time.sleep(t)
for thread in threads:
	thread.join()


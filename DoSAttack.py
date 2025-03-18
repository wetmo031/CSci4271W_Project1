import subprocess

url = "http://localhost:8888/999999/add/full/bookmark123/http%3A%2F%2Fexample.com/example/5"
for i in range(1000):
    subprocess.run(["curl", "-v", url])

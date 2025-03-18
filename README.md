# CSci4271W_Project1

## DoS Attack

After running the bcbmc server, run the DoSAttack.py file to perform a DoS attack.
To do so, run the bcbmc noauth & command to run the server in the background.
Then by running the DoSAttack.py file, it will send 1000 requests to the server.
If you want to change the number of requests, change the attacks variable in the DoSAttack.py file. Additionally, if the serve is not running in noauth mode, the attack will not work as you need the correct auth code.

```bash
bcbmc noauth &
python3 DoSAttack.py
```
# CSci4271W_Project1

## DoS/Tampering Attack

After running the bcbmc server, run the DoSAttack.py file to perform a DoS attack.
To do so, run the bcbmc noauth & command to run the server in the background.
Then by running the DoSAttack.py file, it will send 1000 requests to the server.
If you want to change the number of requests, change the attacks variable in the DoSAttack.py file. Additionally, if the serve is not running in noauth mode, the attack will not work as you need the correct auth code.
When running this script, it will effectively tamper with the bookmarks on record and deny the user the ability to effectively use their bookmark program.
Also, there is a section commented out where you can effectively add infinite bookmarks to the program, which maximises the malicousness of this attack. 

```bash
bcbmc noauth &
python3 DoSAttack.py
```

## Brute Forcing - Spoofing

After the bcbmc server is initialized and an authentication code is set, a simple python script can exploit the lack of possible auth code combinations and no rate limiting protections. By running python3 brute_force.py, pointed by default to the bcbmc server, it will quickly find the proper authentication code and return it to the attacker.

On an already initialized server:
```bash
python3 brute_force.py
```


# Beacon Notify
Small AggressorScript and python script to notify you via Discord when a new beacon checks in.

## Installation
1. Get a discord webhook in Server Settings -> Integrations -> Webhooks -> New webhook
2. Copy the webhook url and paste it in alert.py in the webhookurl variable
3. Get your userid by right clicking your discord name and clicking "Copy id"
4. Paste the id in alert.py in the "ping_id" variable (as a str)
5. Edit discord_notify.cna and replace the "path_to_py" variable with the path to the alert.py file
6. Load the .cna file in the teamserver via the headless AggressorScript console ./agscript
7. Remember to leave the agscript instance running, using linux "screen" utility is what I like to do

e.g.
```
# ./agscript {host and creds etc}
aggressor> load {path to discord_notify.cna}
ctrl^a+d
*exited screen*
exit
```
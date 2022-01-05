import os
import sys
# Your webhook
webhookurl = "https://discord.com/api/webhooks/000000000000000000/aBCDefGhIJKlMNOpQrStuVQxyZ"
# The userid to ping
ping_id = "000000000000000000"
os.system(f'curl --location --request POST "{webhookurl}" --header \'Content-Type: application/json\' --data-raw \'{"content" : "%s, <@{ping_id}>"}\'' % (' '.join(sys.argv[1:])))

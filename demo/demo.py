import requests
from getpass import getpass
import json

# 获取 GitHub 个人API访问令牌的实例代码
# Create an OAuth token for command-line use
# http://bit.ly/lalo7lG

username= 'liuqun' # My GitHub acount
password= '******' # My password
url= 'https://api.github.com/authorizations'
note= 'Mining the Social Web, 2nd Ed.'
post_data= {'scopes':['repo'], 'note': note}
data= json.dumps(post_data)
response= requests.post(
		url,
		auth= (username, password),
		data= data,
	)
print("", response.text)
print("")
msg= response.json()['message']
if msg.startswith("Bad credentials") :
	print("Bad credentials")
elif msg.startswith("Validation Failed") :
	print("Validation Failed")
else :
	print("Your OAuth token is", response.json()['token'])

# Go to https://github.com/settings/applications to revoke this token


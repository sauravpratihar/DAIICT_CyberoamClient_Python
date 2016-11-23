#!/usr/bin/env python
import requests
import sys
import xml.etree.ElementTree as ET
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

student_id = ""
password = ""

if sys.argv[1] != 0:
	if sys.argv[1] == "login":
		data = {"mode":"191",
		"username":student_id,
		"password":password,
		"a":"1479763700530",
		"producttype":"0"}

		p = requests.post("https://10.100.56.55:8090/login.xml",data=data,verify=False)
		myarr = []
		root = ET.fromstring(p.text)
		x = root.findall('message')
		print (x[0].text)
		# print(p.text)


	elif sys.argv[1] == "logout":
		data = {"mode":"193",
		"username":student_id,
		"password":password,
		"a":"1479763700530",
		"producttype":"0"}

		p = requests.post("https://10.100.56.55:8090/login.xml",data=data,verify=False)
		myarr = []
		root = ET.fromstring(p.text)
		x = root.findall('message')
		print (x[0].text)

	else:
		print("provide valid argument. eg. login or logout")


else:
	print("provide valid argument. eg. login or logout")



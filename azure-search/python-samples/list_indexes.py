# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace this with a valid service name.
service_name = 'ENTER SERVICE NAME HERE'

# Replace this with a valid subscription key.
subscriptionKey = 'ENTER KEY HERE'

host = service_name + '.search.windows.net'
operation = '/indexes'
api_version = '2017-11-11'
params = 'api-version=' + api_version
path = operation + '?' + params

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
	return json.dumps(json.loads(content), indent=4)

def get (host, path, content):
	print ('Calling GET ' + host + path + '.')
	headers = {
		'api-key': subscriptionKey,
		'Content-Type': 'application/json',
		'Content-Length': len (content)
	}
	conn = http.client.HTTPSConnection(host)
	conn.request ("GET", path, content, headers)
	response = conn.getresponse ()
	return response.status, response.read ()

status, result = get (host, path, '')
print ('Status code: ' + str(status))
print (pretty_print(result))

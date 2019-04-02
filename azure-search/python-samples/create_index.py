# -*- coding: utf-8 -*-

import http.client, urllib.parse, json

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace this with a valid service name.
service_name = 'ENTER SERVICE NAME HERE'

# Replace this with a valid subscription key.
subscriptionKey = 'ENTER KEY HERE'

index_name = 'test-index'

host = service_name + '.search.windows.net'
operation = '/indexes'
api_version = '2017-11-11'
params = 'api-version=' + api_version
path = operation + '?' + params

index = {
    "name": index_name,
    "fields": [
        { "name": "Id", "type": "Edm.String", "key": "true", "searchable": "false" },
        { "name": "Name", "type": "Edm.String", "searchable": "true" }
    ]
}

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
	return json.dumps(json.loads(content), indent=4)

def post (host, path, content):
	print ('Calling POST ' + host + path + '.')
	headers = {
		'api-key': subscriptionKey,
		'Content-Type': 'application/json',
		'Content-Length': len (content)
	}
	conn = http.client.HTTPSConnection(host)
	conn.request ("POST", path, content, headers)
	response = conn.getresponse ()
	return response.status, response.read ()

# Convert the request to a string.
content = json.dumps(index)
status, result = post (host, path, content)
print ('Status code: ' + str(status))
print (pretty_print(result))

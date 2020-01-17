import requests

def get_json_http():
	res = requests.get('https://jsonplaceholder.typicode.com/todos')
	data = res.json()
	print(data)
	return data

def get_http_with_header():
	headers = {"Content-type": "application/json; charset=UTF-8"}
	params = { "name": "sutin", "lname": "injitt", "age": "30"}
	post_agrs = {
		"headers": headers,
		"params": params
	}

	# res = requests.post(
	# 	'https://jsonplaceholder.typicode.com/todos', 
	# 	params=params, 
	# 	headers=headers)

	res = requests.post(
		'https://jsonplaceholder.typicode.com/todos', **post_agrs)
	print("status code:{:5}, text:{:5}, encodeing: {:5}".format(res.status_code, res.text, res.encoding))
	data = res.json()
	print(data)





if __name__ == '__main__':
	# get_json_http()
	get_http_with_header()

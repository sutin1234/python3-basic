
import requests

# import urllib.request python2
from urllib.request import urlopen

def download_file(url, out_path):
	r = requests.get(url, allow_redirects=True)
	f = open(out_path, 'wb')
	f.write(r.content)

	r.close()
	f.close()

def download_content(url, out):
	opener = urlopen(url)
	print(opener.info()) # get header information
	contents = opener.read()

	write_out = open(out, 'wb')
	write_out.write(contents)

if __name__ == '__main__':
	# download_file('https://www.facebook.com/favicon.ico', 'images/facebook.ico')
	# download_file('http://samui.staging.quo-digital.com/sitemap.xml', 'files/sitemap.xml')
	# download_file(
	# 	'https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf',
	# 	'files/python3_cheat_sheet.pdf'
	# )
	download_content('http://samui.staging.quo-digital.com/', 'web_files/samui.staging.quo-digital.com.html')
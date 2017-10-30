import requests

url="http://www.wechall.net/challenge/wannabe7331/limited_access_too/protected/protected.php"
params={
	#"Cookie":"WC=10001038-38106-imLx9fAu3lO3RqQE",
	"Authorization":"Basic ZW5kdXA6eHhhY3pYWFhBQ1o="
}
r=requests.patch(url,auth=("Authorization","Basic ZW5kdXA6eHhhY3pYWFhBQ1o="))
print (r.text,r.status_code)
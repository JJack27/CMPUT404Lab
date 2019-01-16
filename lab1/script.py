import requests

print(requests.__version__)
r = requests.get("http://www.google.com")


print(r.status_code)
print(r.text)


a = requests.get("https://raw.githubusercontent.com/JJack27/CMPUT404Lab/master/lab1/script.py")
print(a.text)

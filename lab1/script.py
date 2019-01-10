import requests

print(requests.__version__)
r = requests.get("www.google.com")


print(r.status_code)
print(r.text)

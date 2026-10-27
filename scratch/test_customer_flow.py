import urllib.request
import urllib.parse
import http.cookiejar
import re

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# 1. Get login page
resp = opener.open('https://framers-hub-beta.vercel.app/login/')
html = resp.read().decode('utf-8')
csrf = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html).group(1)
print('CSRF Token:', csrf)

# 2. Login as customer
data = urllib.parse.urlencode({'csrfmiddlewaretoken': csrf, 'username': 'test_customer', 'password': 'testpass123'}).encode('utf-8')
req = urllib.request.Request('https://framers-hub-beta.vercel.app/login/', data=data, headers={'Referer': 'https://framers-hub-beta.vercel.app/login/'})
resp2 = opener.open(req)
print('After Login URL:', resp2.geturl())
for cookie in cj:
    print('Cookie:', cookie.name, cookie.value[:10] + '...')

# 3. Access customer dashboard
req3 = urllib.request.Request('https://framers-hub-beta.vercel.app/customer/dashboard/')
resp3 = opener.open(req3)
print('Dashboard URL:', resp3.geturl())

# 4. Access marketplace
req4 = urllib.request.Request('https://framers-hub-beta.vercel.app/marketplace/')
resp4 = opener.open(req4)
print('Marketplace URL:', resp4.geturl())

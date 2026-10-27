import urllib.request
import urllib.parse
import http.cookiejar
import re

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

BASE_URL = 'https://framers-hub-beta.vercel.app'

# 1. Get login page
resp = opener.open(f'{BASE_URL}/login/')
html = resp.read().decode('utf-8')
csrf = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html).group(1)
print('[1] Got CSRF token')

# 2. Login as customer
data = urllib.parse.urlencode({'csrfmiddlewaretoken': csrf, 'username': 'test_customer', 'password': 'testpass123'}).encode('utf-8')
req = urllib.request.Request(f'{BASE_URL}/login/', data=data, headers={'Referer': f'{BASE_URL}/login/'})
resp2 = opener.open(req)
print('[2] Logged in. Landing URL:', resp2.geturl())

# 3. Test Navigation Routes
test_routes = [
    '/customer/dashboard/',
    '/marketplace/',
    '/customer/products/',
    '/customer/marketplace/',
    '/cart/',
    '/orders/',
    '/',
]

print('\n[3] Testing Navigation as Logged-In Customer:')
for route in test_routes:
    req = urllib.request.Request(f'{BASE_URL}{route}')
    res = opener.open(req)
    final_url = res.geturl()
    status = 'OK (Stayed Authenticated)' if 'login' not in final_url or route == '/login/' else 'FAILED (Redirected to login)'
    print(f'   -> Access {route:25} => {final_url:45} [{status}]')

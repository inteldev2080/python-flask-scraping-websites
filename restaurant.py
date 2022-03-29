import requests
from requests.structures import CaseInsensitiveDict
import json

url = "https://e-food.gr/shop/191621/menu"

h = CaseInsensitiveDict()
a = "_gcl_au=1.1.1019796631.1646262550; G_ENABLED_IDPS=google; _ga=GA1.2.1680562085.1646262551; accepted_cookies=true; cookie_privacy_level=personalization; sparks-sid=d60df637-f323-4ea8-aff6-b4b9d2ef536e; language=en_US; _gid=GA1.2.120976903.1647623284; RestaurantMenuCookieTrigger=true; efood_address=%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE+%CE%BA%CE%B1%CE%B9+%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85+4%2C+%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF+%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1%2C+45332; RestaurantListCookieTrigger=true; ci_session=a%3A7%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2243964d38be70227e4dc3400ef967da01%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22188.43.235.177%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A114%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F99.0.4844.74+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1647856877%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22map_data%22%3Ba%3A13%3A%7Bs%3A12%3A%22user_address%22%3Bi%3A0%3Bs%3A7%3A%22address%22%3Bs%3A80%3A%22%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE+%CE%BA%CE%B1%CE%B9+%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85+4%2C+%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF+%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1%2C+45332%22%3Bs%3A8%3A%22latitude%22%3Bs%3A9%3A%2239.665595%22%3Bs%3A9%3A%22longitude%22%3Bs%3A9%3A%2220.851233%22%3Bs%3A4%3A%22city%22%3Bs%3A12%3A%22%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF%22%3Bs%3A6%3A%22county%22%3Bs%3A16%3A%22%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1%22%3Bs%3A6%3A%22street%22%3Bs%3A40%3A%22%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE+%CE%BA%CE%B1%CE%B9+%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85%22%3Bs%3A9%3A%22street_no%22%3Bs%3A1%3A%224%22%3Bs%3A4%3A%22slug%22%3Bs%3A1%3A%22%2F%22%3Bs%3A9%3A%22area_slug%22%3Bs%3A0%3A%22%22%3Bs%3A13%3A%22friendly_name%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22scope%22%3Bs%3A8%3A%22personal%22%3Bs%3A3%3A%22zip%22%3Bs%3A5%3A%2245332%22%3B%7Ds%3A16%3A%22shop_listing_url%22%3Bs%3A662%3A%22https%3A%2F%2Fwww.e-food.gr%2Fshops%3Faddress%3D%25CE%259A%25CE%25B1%25CF%2581%25CE%25B1%25CE%25BF%25CE%25BB%25CE%25AE%2B%25CE%25BA%25CE%25B1%25CE%25B9%2B%25CE%2594%25CE%25B7%25CE%25BC%25CE%25B7%25CF%2584%25CF%2581%25CE%25AF%25CE%25BF%25CF%2585%2B4%252C%2B%25CE%259A%25CE%25AD%25CE%25BD%25CF%2584%25CF%2581%25CE%25BF%2B%25CE%2599%25CF%2589%25CE%25AC%25CE%25BD%25CE%25BD%25CE%25B9%25CE%25BD%25CE%25B1%252C%2B45332%26useraddress%3D0%26user_address%3D0%26latitude%3D39.665595%26longitude%3D20.851233%26city%3D%25CE%259A%25CE%25AD%25CE%25BD%25CF%2584%25CF%2581%25CE%25BF%26county%3D%25CE%2599%25CF%2589%25CE%25AC%25CE%25BD%25CE%25BD%25CE%25B9%25CE%25BD%25CE%25B1%26zip%3D45332%26street%3D%25CE%259A%25CE%25B1%25CF%2581%25CE%25B1%25CE%25BF%25CE%25BB%25CE%25AE%2B%25CE%25BA%25CE%25B1%25CE%25B9%2B%25CE%2594%25CE%25B7%25CE%25BC%25CE%25B7%25CF%2584%25CF%2581%25CE%25AF%25CE%25BF%25CF%2585%26slug%3D%252F%26area_slug%3D%26friendly_name%3D%26scope%3Dpersonal%26street_no%3D4%26nomap%3D0%26msg_chain%3DThe%2BBig%2BBad%2BWolf%26t%3D1647873950%22%3B%7D267b823a3ad6a97735bcf1ed5f9650df5303568e; cf_chl_2=4e444af47009b53; cf_chl_prog=x12; cf_clearance=_17sLdqQaWSp2xaCiJtLSN26qcyuS1tXguJfnXJM0jA-1647897942-0-150; AWSALB=hMIoWGI2BKDS6MIPa5im7tc2Kx8uA30nOPwkJV9Nbptj13Eb4tKdOsGKzJ1NYiq3/kNev0sSGR0CNMdOxmUHw9jE/lGCfTUq6RuOw4NdzP/5sQ+bnc8XfftRPhfr; AWSALBCORS=hMIoWGI2BKDS6MIPa5im7tc2Kx8uA30nOPwkJV9Nbptj13Eb4tKdOsGKzJ1NYiq3/kNev0sSGR0CNMdOxmUHw9jE/lGCfTUq6RuOw4NdzP/5sQ+bnc8XfftRPhfr; __cf_bm=6Uw4t0_F1wtuhLx2ir3WGBJZRlFEgao8zCN3FrjDHrQ-1647897942-0-Adiwxq8xSatSfpnLbm/EbuOC0XqyFSu4+3gW8lg9Gf/notk0GFXqJkFfj/pfKCdVWbHcRzpoDZ4qLPavJIfvnRc=; ab.storage.deviceId.c971c83a-1b96-4bfb-8d59-ccc0a1361dd2=%7B%22g%22%3A%22abcb3eb0-eaff-59e7-4ad3-6a17eed1029d%22%2C%22c%22%3A1646262548713%2C%22l%22%3A1647897707581%7D; ab.storage.userId.c971c83a-1b96-4bfb-8d59-ccc0a1361dd2=%7B%22g%22%3A%225405575%22%2C%22c%22%3A1647564871668%2C%22l%22%3A1647897707581%7D; ab.storage.sessionId.c971c83a-1b96-4bfb-8d59-ccc0a1361dd2=%7B%22g%22%3A%225101b928-346c-2fee-667d-14063b7872d2%22%2C%22e%22%3A1647899508192%2C%22c%22%3A1647897707580%2C%22l%22%3A1647897708192%7D"
h = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
b = "Jan-a.w = January; Feb = February; Mar = March"
r = a.replace("=;", "0000;")
# print(a)
temp = dict(subString.split("=") for subString in r.split("; "))
t = temp["__cf_bm"]
temp["__cf_bm"] = t.replace("0000", "=")
print(temp)
c = json.dumps(temp)
resp = requests.get(url, headers=h, cookies=temp)
print(resp.status_code)
# session = requests.Session()

# response = requests.get('https://e-food.gr/shop/191621/menu')
# cookie=  requests.cookies
# print(cookie)
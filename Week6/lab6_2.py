import urllib.request, urllib.parse, urllib.error
import json
import ssl

MY_SERVICE_URL01 = r"http://py4e-data.dr-chuck.net/json?"
MY_API_KEY01 = 42

try:
    my_ctx01 = ssl.create_default_context()
    my_ctx01.check_hostname = False
    my_ctx01.verify_mode = ssl.CERT_NONE

    my_address01 = input('Enter location: ')
    my_url01 = MY_SERVICE_URL01 + urllib.parse.urlencode({"address": my_address01, "key": MY_API_KEY01})

    print('Retrieving', my_url01)
    my_res_data01 = urllib.request.urlopen(my_url01, context=my_ctx01).read().decode()
    print(f"Retrieved {len(my_res_data01)} characters")
    print(f"Place id {json.loads(my_res_data01)['results'][0]['place_id']}")

except Exception as e:
    print("ERROR!!!", e)
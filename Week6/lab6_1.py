import json
import urllib.request

try:
    my_url01 = input('Enter location: ')
    my_raw_data01 = urllib.request.urlopen(my_url01).read()
    print(f"Retrieving {my_url01}")
    print(f"Retrieved {len(my_raw_data01)} characters")

    my_list01 =  json.loads(data)["comments"]
    print(f"Count: {len(my_list01)}")
    print(f"Sum: {sum([int(x.get('count')) for x in my_list01])}")


except Exception as e:
    print("ERROR!!!", e)
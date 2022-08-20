import urllib.request
import xml.etree.ElementTree as ET

my_url01 = input('Enter location: ')

try:
    my_raw_data01 = urllib.request.urlopen(my_url01).read()
    print(f"Retrieving {my_url01}")
    print(f"Retrieved {len(my_raw_data01)} characters")

    my_list01 =  ET.fromstring(my_raw_data01).findall(r".//count")
    print(f"Count: {len(my_list01)}")
    print(f"Sum: {sum([int(x.text) for x in my_list01])}")

except Exception as e:
    print("ERROR!!!", e)
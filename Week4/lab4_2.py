from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    my_url01 = input("Enter URL: ")
    my_count01 = int(input("Enter count: "))
    my_position01 = int(input("Enter position: "))

    print(f"Retrieving: {my_url01}")
    
    for _ in range(my_count01):
        html = urlopen(my_url01, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        my_anch_pos01 = soup('a')[my_position01-1]
        my_url01 = my_anch_pos01['href']
        cur_name01 = my_anch_pos01.string
        print(f"Retrieving: {my_url01}")

    print(f"Result : {cur_name01}")

except Exception as e:
    print("ERROR!!!", e)
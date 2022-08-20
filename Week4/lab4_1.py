from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

MY_URL01 =  r"http://py4e-data.dr-chuck.net/comments_1629167.html"

try:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    print (sum([int(var01.string) for var01 in BeautifulSoup(urlopen(MY_URL01, context=ctx).read(), "html.parser")('span')]))

except Exception as e:
    print("ERROR!!!", e)
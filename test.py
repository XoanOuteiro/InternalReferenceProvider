# --- Test 1 --- 

from probe import Probe
from curator import Curator
from response_codes import Responses as R
#
#p = Probe()
#
#responseCode, htmldata = p.parse_URL("https://a22xoanmoj.ddns.net")
#
#print(str(responseCode) + " -> " + str(htmldata))


# --- Test 2 ---

p = Probe()

responseCode, htmldata = p.parse_URL("https://a22xoanmoj.ddns.net")

try:

    c = Curator('namelists/common_linked_elements.txt')

except Exception as error:
    print("FileNotFound")

if (responseCode == R.PROBE_REQUEST_SUCCESS):

    data = c.curate(htmldata)
    for l in data:
        print(f'{l[0]} > {l[1]} > {l[2]}')

else:

    print(str(responseCode))
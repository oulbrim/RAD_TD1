"""entrer"""
import httplib
import sys
import pdb
LOG = False
if len(sys.argv) > 2:
    LOG = True
URL = "http://www.python.org/index.html"
if len(sys.argv) > 1:
    URL = sys.argv[1]


def logger(f, message):
    """fonction 1"""
    if LOG:
        f.write(message)

fonc = open("log.txt", "w")
pdb.set_trace()
conn = httplib.HTTPConnection("cache.univ-st-etienne.fr:3128")
logger(fonc, "requete sur : %s\n" % URL)
conn.request("GET", URL)
Reqe = conn.getresponse()
logger(fonc, "Resultat requete : %s %s\n" % (str(Reqe.status), Reqe.reason))
data1 = Reqe.read()
c1 = data1.count(" ")
c = 0
for i in range(len(data1)):
    if data1[i] == " ":
        c1 = c1 + 1
print data1
print c
print c1
conn.close()
fonc.close()

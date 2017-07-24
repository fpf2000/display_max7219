
from xml.dom.minidom import *
import urllib

# Adresse einer XML-Datei
URL = "http://wetter.ringelberger.de/RSS/weewx_rss.xml"

# URL oeffnen und XML Daten einlesen
Baum = urllib.urlopen(URL).read()

# Ausgabe des XML-Baums
print Baum

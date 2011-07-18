# Splits a GPX file into separate files for each track
# Requires Python 2.7 or greater

import xml.etree.ElementTree as etree
import sys

etree.register_namespace("", "http://www.topografix.com/GPX/1/0")

if len(sys.argv) < 2:
  print("Usage gps-split.py <GPX file>")
  sys.exit(1)

tree = etree.parse(sys.argv[1])
root = tree.getroot()

for track in root.findall('{http://www.topografix.com/GPX/1/0}trk'):
  gpx = etree.Element('{http://www.topografix.com/GPX/1/0}gpx', 
      attrib={'creator': 'gpx-split', "version": "1.0"})
  gpx.append(track)

  # in need of error handling, but should work on valid GPX files
  trkpt = track.findall('{http://www.topografix.com/GPX/1/0}trkseg')[0][0]

  # in need of error handling, parses the date part of the first track point
  time = trkpt.findall('{http://www.topografix.com/GPX/1/0}time')[0].text[0:10]

  with open(time + "-mtb.gpx", mode='wb') as f:
    f.write(etree.tostring(gpx))
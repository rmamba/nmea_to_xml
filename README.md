nmea_to_xml
===========

Converts NMEA log files from a GPS unit (Navman MY450LMT) to another format.

Example converting all .log files in directory (./input) to GPX and KML format:
  ```
  python nmea_to_xml.py -gk -i input -o output
  ```

Example joining all .log files to a single KML file in ./output/complete.kml:
  ```
  python nmea_to_xml.py -kj -i input -o output/complete
  ```

Requires: GPSBabel (http://www.gpsbabel.org) and Python (http://www.python.org)

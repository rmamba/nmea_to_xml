"""
    Copyright (C) 2014 Richard Laugesen, richard@tinyrock.com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import os
import sys
from optparse import OptionParser

def convert(input_dir, output_dir, output_formats):
    for format in output_formats:
        for input in os.listdir(input_dir):
            if '.log' in input:
                print format, input

                cmd = 'gpsbabel \
                -i nmea \
                -f "' + os.path.join(input_dir, input) + '" \
                -o ' + format + ' \
                -F ' + os.path.join(output_dir, input[0:-4] + '.' + format)

                os.system(cmd)


if __name__ == "__main__":
    usage = """
    Converts NMEA log files from a GPS unit (Navman MY450LMT) to another format.

    Example converting all .log files in directory (./input) to GPX and KML format:
    python nmea_to_xml.py -gk -i input -o output
    """

    p = OptionParser(usage=usage)
    p.add_option('-i', '--input', dest='input_dir', action='store')
    p.add_option('-o', '--output', dest='output_dir', action='store')
    p.add_option('-k', '--kml', dest='kml', action='store_true', default=False)
    p.add_option('-g', '--gpx', dest='gpx', action='store_true', default=False)
    (opt, args) = p.parse_args()

    formats = []
    if opt.gpx: formats.append('gpx')
    if opt.kml: formats.append('kml')

    if not all([opt.input_dir, opt.output_dir, len(formats) > 0]):
        sys.exit('Try --help')

    convert(opt.input_dir, opt.output_dir, formats)

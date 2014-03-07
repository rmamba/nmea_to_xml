"""
    Copyright (C) 2014 Tiny Rock Pty Ltd

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
import argparse

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


def convert_and_join(input_dir, output_filepath, output_formats):
    for format in output_formats:
        print format
        cmd = 'gpsbabel '

        for input in os.listdir(input_dir):
            if '.log' in input:
                print input
                cmd += ' -i nmea -f "%s"' % os.path.join(input_dir, input)

        cmd += ' -o ' + format + ' -F ' + output_filepath + '.' + format
        os.system(cmd)


if __name__ == "__main__":

    p = argparse.ArgumentParser(description='Converts NMEA log files from a GPS unit (Navman MY450LMT) to another format')
    p.add_argument('-i', '--input', help='Input directory')
    p.add_argument('-o', '--output', help='Output directory (or filepath with --join)')
    p.add_argument('-k', '--kml', action='store_true', help='Generate KML file')
    p.add_argument('-g', '--gpx', action='store_true', help='Generate GPX file')
    p.add_argument('-j', '--join', action='store_true', help='Join all log files and convert into a single output file')
    arg = p.parse_args()

    if not all([arg.input, arg.output]):
        p.error('No directory specified. Add --input and --output')

    if not any([arg.gpx, arg.kml]):
        p.error('No output file format specified. Add --gpx or --kml')

    formats = []
    if arg.gpx: formats.append('gpx')
    if arg.kml: formats.append('kml')

    if arg.join:
        convert_and_join(arg.input, arg.output, formats)
    else:
        convert(arg.input, arg.output, formats)

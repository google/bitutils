# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import argparse
import sys


def _convert(to_base, num):
    return to_base(int(num, 0))[2:]


def _prettify(bits, options):
    result = [options.prefix]
    if options.width:
        result.append('0' * max(0, options.width - len(bits)))
    result.append(bits)
    return ''.join(result)


def main(to_base, prefix, unit_name):
    parser = argparse.ArgumentParser()
    parser.add_argument('number', nargs='*', default=None)
    parser.add_argument(
        '-w',
        type=int,
        help=unit_name+' width to format as',
        metavar='WIDTH',
        dest='width')
    parser.add_argument(
        '-P',
        action='store_const',
        const='',
        default=prefix,
        help='disable `'+prefix+'` prefix',
        dest='prefix')
    options = parser.parse_args()

    if options.number:
        for number in options.number:
            print(_prettify(_convert(to_base, number), options))
    else:
        for line in sys.stdin:
            print(_prettify(_convert(to_base, line.strip()), options))

# myls.py
import argparse
import os
import sys

import imagecollector.parser

# Create the parser
my_parser = imagecollector.parser.ImageCollectorCliParser()
# Execute the parse_args() method
args = my_parser.parse_args()

# a[href*="https://www.reddit.com/login/"]

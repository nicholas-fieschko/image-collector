# myls.py
import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog='image-collector',
                                    description='Scrape and download images from saved collections:'
                                    + ' the Tumblr draft storage or Reddit saved posts')

# Add the arguments
my_parser.add_argument('Site',
                       metavar='site',
                       type=str,
                       choices=['tumblr', 'reddit'],
                       help='the site to scrape. valid options are "tumblr" or "reddit"')

my_parser.add_argument('Username',
                       metavar='username',
                       type=str,
                       help='the username of the account to log in to on the target website')

my_parser.add_argument('Password',
                       metavar='password',
                       type=str,
                       help='the password of the account to log in to on the target website')

outputModeGroup = my_parser.add_mutually_exclusive_group(required=True)
outputModeGroup.add_argument('--folder', '-f',
                             dest='folder',
                             type=str,
                             help='the folder to download images to, relative to root',
                             default='images')

outputModeGroup.add_argument('--html',
                             dest='IsHtmlMode',
                             action='store_true',
                             help='create an html page with the scaraped images embedded, without downloading')

# Execute the parse_args() method
args = my_parser.parse_args()

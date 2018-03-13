#!/usr/bin/env python

"""

redditr0n: A generic subreddit crawler built on PRAW.

"""

import sys
import argparse
import ConfigParser
import praw

# Setup command-line interface
cli = argparse.ArgumentParser(description=__doc__)
cli.add_argument('config_file', help='path to configuration file')

# Parse command-line arguments
args = cli.parse_args()

config_file = args.config_file

# Define configuration file format
config_section_name = 'redditr0n'
config_option_names = ['client_id', 'client_secret', 'user_agent']

# Parse configuration file
config = ConfigParser.RawConfigParser()

try:
    with open(config_file, 'r') as f:
        config.readfp(f)
except IOError:
    sys.exit('ERROR: Could not read configuration file')

try:
    config_options = {option: config.get(config_section_name, option) for option in config_option_names}
except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
    sys.exit('ERROR: Configuration file format incorrect. See \'config.ini.example\'')

# Main program
print config_options

reddit = praw.Reddit(client_id=config_options['client_id'],
                     client_secret=config_options['client_secret'],
                     user_agent=config_options['user_agent'])

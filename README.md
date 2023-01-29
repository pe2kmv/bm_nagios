# Brandmeister Nagios plugin

## Introduction
This script checks the connection of a repeater to the Brandmeister master. The connection is checked by verifying whether or not the repeater callsign is included in the list of connected repeaters. This list is pulled from the master in JSON format. Succesfull verification returns the exit code '0' ('OK') and failed verification returns exit code '3' ('CRITICAL').

## Dependencies
This script has been written in Python 3. Furthermore it depends on some additional libraries for Python:
- requests (to query the API)
- json (to translate the json data)
- argparse (to parse the arguments from the command line into the script)
- sys (to generate the correct exit codes)

Please consult the omniscient internet for assistance on these topics.

## Installation
Pull the repository to your local computer
```
git pull https://github.com/pe2kmv/bm_nagios.git
```
Then copy the script to a directory of your choice, for instance:
```
cp ./bm_nagios/bm_nagios.py /usr/lib/nagios/plugins/

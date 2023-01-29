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
```
Add the following lines to the Nagios commands file **commands.cfg**
```
define command{
        command_name    check_brandmeister_con
        command_line    /usr/lib/nagios/plugins/bm_nagios.py $ARG1$ $ARG2$
}
```
Now the command is available to be included in a server configuration file. Use the example below to check the connection of a specific repeater  to a predetermined master (**remove the square brackets from this example!**):
```
check_command           check_brandmeister_con!http://[MASTER_SERVER_URL]/status/monitor.php![REPEATER_CALLSIGN]

## The small printed stuff
* always be sure to have a backup of your configuration files before messing around
* use at your own risk
* not meant for business critical environments
* no support. If it works: GREAT. If not: please feel free to change it at your convenience

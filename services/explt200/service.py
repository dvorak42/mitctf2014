#!/usr/bin/python

import subprocess

subprocess.call(['socat', 'TCP-LISTEN:4320,reuseaddr,fork', 'EXEC:\'./sandbox.py\',pty,ctty,echo=0'])

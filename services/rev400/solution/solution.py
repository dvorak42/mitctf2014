#!/usr/bin/python

import os
import subprocess
os.setresgid(7331, 7331, 7331)
os.setresuid(7331, 7331, 7331)
subprocess.call('./service')

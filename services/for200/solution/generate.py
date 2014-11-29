#!/usr/bin/python

import subprocess

host_ip = 'REMOTE.COM'

subprocess.call(['dot', '-Tpdf', 'main.dot', '-O'])
subprocess.call(['mv', 'main.dot.pdf', 'main.pdf'])

subprocess.call(['cp', '-r', 'machine', 'service'])
subprocess.call(['sed', '-i', 's/\\$\\$ATTACKER_IP\\$\\$/%s/g' % (host_ip), 'service/var/log/apache2/access.log'])
subprocess.call(['sed', '-i', 's/\\$\\$ATTACKER_IP\\$\\$/%s/g' % (host_ip), 'service/var/log/apache2/error.log'])

subprocess.call(['mkdir', 'fexploits'])
subprocess.call(['cp', 'exploit.sh', 'fexploits/'])
subprocess.call(['cp', 'main.pdf', 'fexploits/'])
#subprocess.call(['scp', '-r', 'fexploits/', 'root@%s:/var/www/' % (host_ip)])
subprocess.call(['rm', '-r', 'fexploits/'])
subprocess.call(['zip', '-r', 'service.zip', 'service/'])
subprocess.call(['rm', '-rf', 'service/'])

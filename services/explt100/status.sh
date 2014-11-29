#!/usr/bin/shellshock

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<title>Asteroid Mining System Status</title>'
echo '</head>'
echo '<body>'

echo '<h3>'
echo -n 'Current Mining Speed: '
uptime | sed 's/.*: //g; s/,.*//g'
echo '</h3>'

echo -n '<h3>Uptime: '
uptime
echo '</h3>'

echo '</body>'
echo '</html>'

exit 0

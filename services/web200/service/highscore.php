<?php
header("X-XSS-Protection: 0");

if($_REQUEST['score']) {
  $score = $_GET['score'];
  $person = $_GET['person'];
  $link = $_GET['link'];
  setcookie('isadmin', 'false');
  setcookie('user', $person);
  echo "<center>Adding New Record: " . $person . " achieved score " . $score . ". Linking to " . $link . "</center>";
  echo "<center>Links will be manually verified by the administrator before being displayed.</center>";
  $line = base64_encode(htmlspecialchars($score) . ':::SECRET:::' . htmlspecialchars($person) . ':::SECRET:::' . htmlspecialchars($link) . ':::SECRET:::0');
  $f = fopen("scores", "a");
  fwrite($f, $line . "\n");
  fclose($f);
}

if($_COOKIE['isadmin'] == 'true') {
  echo "<center>NICE TRY. BUT THE FLAG IS ONLY IN THE REAL ADMIN'S COOKIE.</center>";
}

$f = fopen("scores", "r");
$data = fread($f, filesize("scores"));
fclose($f);

$darr = explode("\n", $data);
?>
<center>
<h1>High Scores:</h1>
<table>
<?php
foreach($darr as $l) {
  $lb = base64_decode($l);
  $la = explode(':::SECRET:::', $lb);
  $score = $la[0];
  $name = $la[1];
  $link = $la[2];
  $approved = $la[3];
  if(count($la) != 4) {
    continue;
  }
  if($approved == '+') {
    echo "<tr><td>" . $name . "</td><td>" . $score . "</td><td><a href=\"" . $link . "\">" . $link . "</a></td></tr>";
  } else if($approved == '-') {
    echo "<tr><td>" . $name . "</td><td>" . $score . "</td><td>HIDDEN</td></tr>";
  } else {
    echo "<tr><td>" . $name . "</td><td>" . $score . "</td><td>-</td></tr>";
  }
}
?>
</table>
</center>
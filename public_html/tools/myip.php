<html>
<head>
  <title>:: my ip ::</title>
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link href='http://fonts.googleapis.com/css?family=Droid+Sans+Mono' rel='stylesheet' type='text/css'>
  <style>
    body {font-family: 'Droid Sans Mono', arial, serif; }
  </style>
</head>

<body>
  <?php print "IP number: ";print $_SERVER['REMOTE_ADDR']?>
  <br>
  <?php print "Host name: ";print gethostbyaddr($_SERVER['REMOTE_ADDR'])?>
</body>
</html>

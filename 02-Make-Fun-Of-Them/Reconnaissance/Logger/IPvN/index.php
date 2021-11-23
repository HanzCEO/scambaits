<?php
header("Content-Type: text/plain");
echo $_SERVER['HTTP_X_FORWARDED_FOR'] ?: $_SERVER['REMOTE_ADDR'];
?>

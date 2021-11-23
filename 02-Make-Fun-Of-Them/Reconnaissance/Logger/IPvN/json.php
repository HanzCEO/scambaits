<?php
header("Content-Type: application/json");

function get($url) {
	if (function_exists("curl_init")) {
		// Use cURL
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

		$data = curl_exec($ch);
		curl_close($ch);
		return $data;
	} else {
		return file_get_contents($url);
	}
}

$public_ip = $_SERVER['HTTP_X_FORWARDED_FOR'] ?: $_SERVER['REMOTE_ADDR'];

$data = json_decode(get("http://ip-api.com/json/$public_ip?fields=66846719"), true);
$data['ip'] = $data['query'];
$data['user_agent'] = $_SERVER['HTTP_USER_AGENT'];
$data['accept'] = $_SERVER['HTTP_ACCEPT'];

unset($data['query']);

echo json_encode($data);
?>

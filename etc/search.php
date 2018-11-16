<?php

class sj_tf_tv {
	private $qurl = 'http://localhost/tfreeca/sj_tf.php?sc=';

	public function __construct() {
	} 

	public function prepare($curl, $query) {
		$url = $this->qurl . urlencode($query);
		curl_setopt($curl, CURLOPT_URL, $url);
	} 
	
	public function parse($plugin, $response) {
		return $plugin->addRSSResults($response);
	}
}

?>

<?php
include 'func.php';

/*
    https://github.com/Fuziro
    Made by Avindeso
*/

$init = new Bom();

//Eksekusi Call/Sms Boomber (Limit 200x/Jam)
$init->type = 2; //Type 2 untuk telpon, Type 1 untuk sms
$init->no = ""; //Nomer Hp tujuan

if ($init->type == 1) {
	for ($i=0; $i < 2; $i++) { 
	    $init->Verif($init->no,$init->type);
	}
}elseif ($init->type == 2) {
	 $init->Verif($init->no,$init->type);
}

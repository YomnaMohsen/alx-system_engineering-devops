# increase unlimit
exec {'fix-nginx':
    command => 'sed -i s/15/4096/ /etc/default/nginx',
    path    => 'usr/local/bin/:/bin/'
}

# Restart nginx
~>exec {'restart':
    command => 'nginx restart'
    path    => '/etc/init.d/'
}
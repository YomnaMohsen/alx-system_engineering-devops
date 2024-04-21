# make changes to configuration file
include stdlib
file_line {'Password auth no':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    replace => true,
}

file_line {'conf private key':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    replace => true,
}

# execute pkill command
exec{'kill-process':
    command => 'pkill killmenow',
    path    => '/usr/bin',
}
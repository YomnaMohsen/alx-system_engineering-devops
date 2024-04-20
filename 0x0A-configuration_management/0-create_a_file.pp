# create file with certain content
file{'/tmp/school':
  ensure  => 'ensure'
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}

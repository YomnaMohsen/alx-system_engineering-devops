# Postmortem
## Issue Summary
Upon the release of Alx-africa 0x17 web_stack_debugging task at <B> 4 June 2024 6 AM EAT </B> and ended around  <B> 8:00 AM EAT </B>. 

A problem occured in ubuntu container which has a running apache web server. a Get request in server led to 500 "Internal Server Error". Instead, an expected response is a simple HTML page define alx-wordpress site

## Impact: 
This temprary Internal Server Error, resulting in degrading the perfromance of services provided by this server, as server can't respond to any user's request

## Root Cause
Misconfiguration of some files

<br></br>

# Maintaince process

1) Start to check running processes using "ps aux | grep apache", we found 2 apache processes (root and www-data) are properly running


2) Start to open another terminal using tmux , so in one terminal , I ran strace on PID of root Apache server and curled in another terminal, But no clear conclusion obtained

3) Repeat step 2, with strace on PID of www-data apache server, but this time the result is very intersting. strace revelead "-1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp"

4) Searching through files in /var/www/html one-by-one, start using vim for locating erroneous .phpp extension and finally found it in wp-settings.html

5) Fux the typo and now curl return 200 ok!

6) Wrote a Puppet manifest to automate error fixing.


# Corrective and Preventative Measures:

This wasn't a server error but application error

1) Test the application before deployment

2) Monitoring service must be enabled

In response to this error, a puppet mainfest had been written for fixing identical error that may occur in future, the mainfest replaces any "phpp" with "php" in /var/www/html/wp-settings.php

I hope this error never occur again ;)
Recover MySQL root Password
===========================

* Enter super user root account sudo su
* Stop mysql service service mysqld stop
* And enter safe mode mysqld_safe --skip-grant-tables &
* Login mysql shell with root mysql -u root mysql
* On mysql shell
* update user set password=PASSWORD("<Your New Password>") where user='root';
* flush privileges;
* restart mysql sudo service mysqld restart

NB: to recover your original password without changing it, you need to crack it.

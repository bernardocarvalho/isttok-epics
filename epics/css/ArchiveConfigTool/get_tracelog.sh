#!/bin/bash
#mysql -u report -p"\$report" -D archive -e 'SELECT `smpl_time`, `severity_id`, `status_id`, `str_val` FROM `sample` WHERE `channel_id` = 12'
#mysql -u report -p"\$report" -D archive <<< 'show tables'
#mysql -u report -p"\$report" -D archive <<< "SELECT `smpl_time`, `severity_id`, `status_id`, `str_val` FROM `sample` WHERE `channel_id` = 13"
mysql -u report -p"\$report" -D archive <<< 'SELECT  `smpl_time`, `str_val` , `severity_id`, `status_id` FROM sample WHERE channel_id = 12 ORDER by `smpl_time` DESC LIMIT 20'

#"SELECT `smpl_time`, `severity_id`, `status_id`, `str_val` FROM `sample` WHERE `channel_id` = 13"


#!/bin/bash
echo -e "\n127.0.0.1\tpwn18\n::1\tpwn18" >> /etc/hosts
service ssh restart

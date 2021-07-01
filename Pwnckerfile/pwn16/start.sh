#!/bin/bash
echo -e "\n127.0.0.1\tpwn16\n::1\tpwn16" >> /etc/hosts
service ssh restart

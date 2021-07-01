#!/bin/bash
echo -e "\n127.0.0.1\tpwn20\n::1\tpwn20" >> /etc/hosts
service ssh restart

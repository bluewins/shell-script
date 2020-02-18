#!/bin/sh
# Zabbix Install Script
# https://repo.zabbix.com/zabbix/
# 공인 연결이 되어 있을 경우 사용

OS=`uname -r`
HOSTNAME=`hostname`
ZIP='192.168.0.xxx.'

if [[ "$OS" == *"el6"* ]];then
    wget https://repo.zabbix.com/zabbix/4.0/rhel/6/x86_64/zabbix-agent-4.0.15-1.el6.x86_64.rpm
    rpm -ivh zabbix-agent-4.0.15-1.el6.x86_64.rpm
    sed -i "98s/.*/Server=$ZIP/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "139s/.*/ServerActive=$ZIP:10051/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "150s/.*/Hostname=$HOSTNAME/g" /etc/zabbix/zabbix_agentd.conf
    chkconfig zabbix-agent on
    service zabbix-agent restart
elif [[ "$OS" == *"el7"* ]];then
    wget https://repo.zabbix.com/zabbix/4.0/rhel/7/x86_64/zabbix-agent-4.0.15-1.el7.x86_64.rpm
    rpm -ivh zabbix-agent-4.0.15-1.el7.x86_64.rpm
    sed -i "98s/.*/Server=$ZIP/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "139s/.*/ServerActive=$ZIP:10051/g" /etc/zabbix/zabbix_agentd.conf
    sed -i "150s/.*/Hostname=$HOSTNAME/g" /etc/zabbix/zabbix_agentd.conf
    systemctl start zabbix-agent.service
    systemctl enable zabbix-agent.service
fi
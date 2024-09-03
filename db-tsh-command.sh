#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: $0 <port_forward> <ip_address>"
    exit 1
fi

port_forward="$1"
ip_address="$2"

tsh ssh -L $port_forward kishormuruganandham@$ip_address

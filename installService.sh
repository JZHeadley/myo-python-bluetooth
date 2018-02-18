#!/bin/bash
cp ./MyOwnFreedomClient.service /etc/systemd/system/
systemctl daemon-reload
systemctl start MyOwnFreedomClient

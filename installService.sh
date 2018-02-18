#!/bin/bash
cp ./MyOwnFreedomClient.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable MyOwnFreedomClient
systemctl start MyOwnFreedomClient

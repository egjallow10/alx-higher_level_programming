#!/bin/bash
#A script to send a delete request 
curl -s -X OPTIONS "$1" -i | grep Allow | cut -d ' ' -f2-

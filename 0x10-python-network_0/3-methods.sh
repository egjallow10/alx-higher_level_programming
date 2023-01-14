#!/bin/bash
#A script to send a delete request 
curl -s -X OPTIONS "$url" -i | grep Allow | cut -d ' ' -f2-

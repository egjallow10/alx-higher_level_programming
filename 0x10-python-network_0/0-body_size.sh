#!/bin/bash
#A script to print the content length
curl -s -w "%{size_download}" -o /dev/null  '$1'

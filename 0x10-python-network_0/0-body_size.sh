#!/bin/bash
#A script to print the content length
curl -s $1 | wc -c 

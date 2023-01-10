#!/bin/bash
#A script to print the status code
curl -s -w "%{response_code}" $1 

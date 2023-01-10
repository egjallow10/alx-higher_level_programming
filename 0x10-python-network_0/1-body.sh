#!/bin/bash
#A script to print the status code
curl -sL -w "%{response_code}" $1 

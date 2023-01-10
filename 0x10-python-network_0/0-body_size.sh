#!/bin/bash
#A script to print the content length
curl -s | wc -c '$1'

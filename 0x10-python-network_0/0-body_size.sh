#!/bin/bash
#A script to print the content length
response=(curl -s $1) && echo ${#response}
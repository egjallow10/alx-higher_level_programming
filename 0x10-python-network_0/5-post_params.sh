#!/bin/bash
#A script to send a  request with a header
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
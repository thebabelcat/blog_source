#!/bin/bash

if [[ -z $1 ]]; then echo "$0 FILE"; exit 1; fi

file=$1

tesseract -l ita --oem 1 --psm 1 $1 $1

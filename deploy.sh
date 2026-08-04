#!/bin/bash

./build-css.sh 

cd pelican
make publish
cd ..

rm -fR deploy/*
cp -R pelican/output/* deploy/

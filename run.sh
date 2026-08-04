#!/bin/bash

./build-css.sh

cd pelican
pelican -lrv $@

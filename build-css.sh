#!/bin/bash
# Compile memento SCSS to CSS.
# Pass --watch to keep it running and recompile on save.
set -e

cd memento
sass --no-source-map "$@" scss/custom.scss static/css/custom.css

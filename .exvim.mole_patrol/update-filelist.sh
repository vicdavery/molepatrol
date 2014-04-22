#!/bin/bash
export DEST="./.exvim.mole_patrol"
export TOOLS="/home/dave/development/main/vimfiles/tools/"
export FOLDERS="./src,./test"
export FILE_SUFFIXS=".*"
export TMP="${DEST}/_files"
export TARGET="${DEST}/files"
sh ${TOOLS}/shell/bash/update-filelist.sh

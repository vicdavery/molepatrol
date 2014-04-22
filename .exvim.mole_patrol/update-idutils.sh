#!/bin/bash
export DEST="./.exvim.mole_patrol"
export TOOLS="/home/dave/development/main/vimfiles/tools/"
export EXCLUDE_FOLDERS=""
export TMP="${DEST}/_ID"
export TARGET="${DEST}/ID"
sh ${TOOLS}/shell/bash/update-idutils.sh

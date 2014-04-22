#!/bin/bash
export DEST="./.exvim.mole_patrol"
export TOOLS="/home/dave/development/main/vimfiles/tools/"
export CTAGS_CMD="ctags"
export OPTIONS=""
export TMP="${DEST}/_tags"
export TARGET="${DEST}/tags"
sh ${TOOLS}/shell/bash/update-tags.sh

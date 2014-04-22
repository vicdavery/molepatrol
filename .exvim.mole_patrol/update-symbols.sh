#!/bin/bash
export DEST="./.exvim.mole_patrol"
export TOOLS="/home/dave/development/main/vimfiles/tools/"
export TMP="${DEST}/_symbols"
export TARGET="${DEST}/symbols"
sh ${TOOLS}/shell/bash/update-symbols.sh

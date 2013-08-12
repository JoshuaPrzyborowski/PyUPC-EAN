#!/usr/bin/env sh

if [ ! -z "${PYTHON}" ]; then
 export PYTHON
else
 export PYTHON="$(/usr/bin/which python)"
fi
if [ "$1" = "setup" ] || [ "$1" = "install" ]; then
 PYTHON="${PYTHON}" ./setup
else
 PYTHON="${PYTHON}" PYTHONDONTWRITEBYTECODE="x" PYTHONPATH="$(pwd)/upcean" "${PYTHON}" -b -B -x "./upc.py" "$@"
fi

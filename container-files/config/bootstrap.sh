#!/usr/bin/env bash

set -e
set +x 

# Supervisord default params
SUPERVISOR_PARAMS='-c /etc/supervisord.conf'

#if [ "$(ls /config/init/)" ]; then
#  for init in /config/init/*.sh; do
#    . $init
#  done
#fi

# Add new users
if [ -n "$PASSWDFILE" ]; then
  echo '$PASSWDFILE is set:' $PASSWDFILE
#  chmod +x /Users/nehalingareddy/neha_test/python_api/python/new/wookiee2187/container-files/config/init/new.sh
  bash config/init/new.sh $PASSWDFILE
#/Users/nehalingareddy/neha_test/python_api/python/new/wookiee2187/container-files/config/init/new.sh $PASSWDFILE
else
  echo '$PASSWDFILE not defined! Not creating users'
fi

supervisord -n $SUPERVISOR_PARAMS

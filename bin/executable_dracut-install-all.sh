#!/usr/bin/env bash

/usr/bin/ls -1 /usr/lib/modules/*/pkgbase | cut -c 2- | /usr/local/bin/dracut-install.sh

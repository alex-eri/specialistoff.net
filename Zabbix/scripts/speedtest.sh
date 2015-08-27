#!/bin/sh

speedtest-cli --timeout 30 --server $1 > /tmp/speedtest

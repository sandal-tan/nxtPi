#!/bin/bash
# Scans for the PiBot network
# For use with the Remote.app
# Ian Baldwin, 5/19/13
PiBotUp=$(airport -s | grep -c PiBot)
if [ "$PiBotUp" == 1 ]; then
echo Network 'PiBot' Found
else
echo Unable to find network 'PiBot'
fi

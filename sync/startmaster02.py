#!/bin/bash
/usr/bin/omxplayer-sync -mu -o both /media/internal/video/02* > /dev/null 2>&1 & echo $! &

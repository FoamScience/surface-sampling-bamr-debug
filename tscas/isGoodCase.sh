#!/usr/bin/bash
if test `grep 'End' log.interIsoFoam`; then echo 1; else echo 0; fi

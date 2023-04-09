#!/bin/bash
clear
pycodestyle commands.py 
pycodestyle commands.py | wc -l
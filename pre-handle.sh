#!/bin/bash
cat "Fluorine in Si- H.txt" | grep "eV"  | grep -v "Stop" | grep -v "/" > "a.out"

python test.py $1
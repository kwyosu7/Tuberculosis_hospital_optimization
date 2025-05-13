#!/bin/bash

# 0부터 20까지 1씩 증가
for a in $(seq 2014 1 2022); do
    echo "a: $a"
	python3 optimization.py $a &
done

#!/bin/bash

# 0부터 20까지 1씩 증가
for a in $(seq 0 1 20); do
    echo "a: $a"
	python3 at_b_optimization.py $a &
done

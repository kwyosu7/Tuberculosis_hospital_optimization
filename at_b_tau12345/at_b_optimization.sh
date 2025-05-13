#!/bin/bash

# # 0부터 20까지 1씩 증가
for a in $(seq 0 1 9); do
    echo "a: $a"
	spg run csg2 /miniconda3/envs/YongsungKwon_env_py310/bin/python at_b_optimization.py $a & 
	sleep 1s

done

# 0부터 20까지 1씩 증가
# for a in $(seq 10 1 30); do
#     echo "a: $a"
# 	python3 at_b_optimization.py $a &
# done

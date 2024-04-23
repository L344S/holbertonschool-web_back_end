# Python - Async Comprehensions

## Description

This project is part of the Holberton School's web back-end training program. It focuses on the use of asynchronous comprehensions and generators in Python 3.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Tasks
- 0. Async Generator
- 1. Async Comprehensions
- 2. Run time for four parallel comprehensions

## Files

- `0-async_generator.py`: Contains the coroutine `async_generator` that yields a random number after waiting for 1 second.
- `1-async_comprehension.py`: Contains the coroutine `async_comprehension` that collects 10 random numbers using an async comprehending over `async_generator`.
- `2-measure_runtime.py`: Contains the coroutine `measure_runtime` that measures the total runtime for executing `async_comprehension` four times in parallel.

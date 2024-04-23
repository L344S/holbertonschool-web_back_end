# Python - Async

## Learning Objectives
- async and await syntax
- How to execute an async program with asyncio
- How to run concurrent coroutines
- How to create asyncio tasks
- How to use the random module

## Files

- `0-basic_async_syntax.py`: Contains the function `wait_random` that waits for a random delay and eventually returns it.
- `1-concurrent_coroutines.py`: Contains the function `wait_n` that spawns `wait_random` n times and returns the list of all the delays.
- `2-measure_runtime.py`: Contains the function `measure_time` that measures the total execution time for `wait_n(n, max_delay)`.
- `3-tasks.py`: Contains the function `task_wait_random` that returns a asyncio.Task.
- `4-tasks.py`: Contains the function `task_wait_n` that is similar to `wait_n` but calls `task_wait_random`.


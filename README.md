# Cracking the Coding Interview in Python

Modern Python (3.12+) implementations of every chapter and problem in *Cracking the Coding Interview* (6th ed.), one Jupyter notebook per chapter.

Problem statements are **paraphrased** and all code is original. The notebooks are meant to be read alongside the book, not in place of it.

## Layout

| Folder | Book chapter | Problems |
|---|---|---|
| `00_big_o` | VI. Big O | runtime experiments + examples |
| `01_arrays_and_strings` | 1 | 1.1 – 1.9 (+ hash table) |
| `02_linked_lists` | 2 | 2.1 – 2.8 |
| `03_stacks_and_queues` | 3 | 3.1 – 3.6 |
| `04_trees_and_graphs` | 4 | 4.1 – 4.12 (+ heap, trie, BFS/DFS) |
| `05_bit_manipulation` | 5 | 5.1 – 5.8 |
| `06_math_and_logic_puzzles` | 6 | 6.1 – 6.10 (each verified by simulation/brute force) |
| `07_object_oriented_design` | 7 | 7.1 – 7.12 |
| `08_recursion_and_dynamic_programming` | 8 | 8.1 – 8.14 |
| `09_system_design_and_scalability` | 9 | 9.1 – 9.8 (runnable toy models) |
| `10_sorting_and_searching` | 10 | 10.1 – 10.11 (+ merge/quick/radix sort) |
| `11_testing` | 11 | 11.1 – 11.6 (as `unittest` suites) |
| `12_c_and_cpp` | 12 | 12.1 – 12.11 (Python analogues, `ctypes` for raw memory) |
| `13_java` | 13 | 13.1 – 13.8 (Python analogues) |
| `14_databases` | 14 | 14.1 – 14.7 (real SQL on in-memory `sqlite3`) |
| `15_threads_and_locks` | 15 | 15.1 – 15.7 |
| `16_moderate` | 16 | 16.1 – 16.26 |
| `17_hard` | 17 | 17.1 – 17.26 |
| `18_advanced_topics` | XI. Advanced Topics | topo sort, Dijkstra, open addressing, Rabin–Karp, AVL, red–black, MapReduce |

Each problem cell contains:
1. a short paraphrased prompt and the key insight,
2. one or more implementations (brute force → optimal where instructive), with complexity notes,
3. `assert`-based tests, often checked against a brute-force reference on random inputs.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run jupyter lab
```

## Verify every notebook

```bash
uv run python tools/run_all.py            # all chapters
uv run python tools/run_all.py 04 17      # just chapters 4 and 17
```

## Conventions

- Only the standard library is used inside notebooks (no extra installs needed).
- Type hints, `dataclass`es, `match`, `functools.cache`, `heapq`, `bisect`, `collections`, and `graphlib` are used where they're the idiomatic tool.
- Where Python differs from the book's Java assumptions, the notebook says so. Examples: arbitrary-precision ints in Chapter 5, the GIL in Chapter 15, and immutable strings in Chapter 1.

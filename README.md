# Minimum Edit Distance

The similarity between two strings may be measured in many ways. One of such a string metric is known as the Levenshtein distance, which is a type of edit distance.

The edit distance between two strings is the minimum number of single-character insertions, deletions, or substitutions required to change one string into the other.

The class `Levenshtein.py` implements the **[Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm)** allowing to pass **varying costs** for insertion, deletion and substitution.

For more info on Levenshtein distance, refer [wiki](https://en.wikipedia.org/wiki/Levenshtein_distance).

## Requirements

- Python 3.6+
- No dependencies on any other library

## Usage

```python
from Levenshtein import Levenshtein

source = "hello"
target = "world"

l = Levenshtein(source, target, costs=(1, 1, 2))

min_distance = l.distance()
# min_distance = 4

operations = l.edit_ops()
# operations =
# [{'type': 'Substitution', 'i': 0, 'j': 0},
#  {'type': 'Substitution', 'i': 1, 'j': 1},
#  {'type': 'Substitution', 'i': 2, 'j': 2},
#  {'type': 'Match',        'i': 3, 'j': 3},
#  {'type': 'Substitution', 'i': 4, 'j': 4}]

l.print_distance_matrix()
# Distance Matrix:
# -  -  w  o  r  l  d
# -  0  2  4  6  8 10
# h  2  1  3  5  7  9
# e  4  3  2  4  6  8
# l  6  5  4  3  4  6
# l  8  7  6  5  3  5
# o 10  9  7  7  5  4

l.print_edit_ops()
# Edit Operations:
# Type           i  j
# --------------------
# Substitution   0  0
# Substitution   1  1
# Substitution   2  2
# Match          3  3
# Substitution   4  4
```

Check out `Levenshtein.py` for more details.

## Authors

[Mayank Jain](https://github.com/mayank-02)

## License

MIT

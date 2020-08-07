# Bit Mining, Iteration, and Base Conversion

Tools for iterating through keyspaces and demonstrating how bit mining works.

### simple_brute.py
Create every permutation up to length "max_length" with a given keyspace.
Specify action to take for each permutation. Ex:
* Compare permutation digest to digests from list
* Print every nth permutation

Convert between baseN permutation and base10 value with base10_to_n and n_to_base10.

### mine_demo.py
Demonstrations of priv/ pub key creation and finding hash values below threshold.

### base_convert.py
Convert between base10 to baseN with a given keyspace. Ex:
* Binary
* Hexadecimal
* Ternary
* etc.
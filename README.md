# Alphabet Trie Dictionary

This project implements an alphabet trie (prefix tree) data structure in Python, allowing efficient storage and retrieval of strings of alphabets.

## Features

- Insert words into the trie
- Search for words in the trie
- Avoids duplicate entries

## Technologies

- Python 3.9
- Tree Data Structure
## Usage

1. Initialize the Trie:
    ```python
    from alphabet_trie import alphabet
    trie = alphabet()
    ```
2. Insert a word:
    ```python
    trie.insert("example")
    ```
3. Search for a word:
    ```python
    exists = trie.search("example")
    print(exists)  # Output: True or False
    ```

## Contact

Muhammad Ietazaz Aslam - ietazazaslam2001@gmail.com

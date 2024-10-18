# 🔒 Bloom Filter Password Checker

Bloom Filter Password Checker is a fast and memory-efficient tool to check if a password is **likely** present in a dictionary of common passwords. Using a **Bloom Filter**, it provides rapid membership testing with a configurable false positive rate, all while keeping memory usage minimal.

## ✨ Features

- **High Efficiency**: Uses a bit array to store passwords with optimal space utilization.
- **Blazing Fast Lookups**: Quickly checks if a password is weak using multiple hash functions.
- **Customizable Accuracy**: Adjustable false positive rate to suit different accuracy needs.

## 📂 Setup

1. Place your dictionary files containing lists of passwords into the `dict/` directory.
2. Run the script to initialize the Bloom Filter based on the total number of passwords and the chosen false positive rate.
3. Input passwords to check if they are weak (i.e., likely present in the dictionary).

## ⚙️ Customization

- **Storage Size**: Define the maximum number of passwords to be stored.
- **False Positive Rate**: Adjust the error rate to balance between memory usage and accuracy.

The tool automatically computes the optimal size for the bit array and the number of hash functions based on these inputs.

## ⏱ Performance Insights

- **Time Tracking**: The script measures and prints the time taken for:
  - Reading and counting passwords from files.
  - Populating the Bloom Filter with dictionary words.
  
  This allows for performance monitoring when handling large datasets.

## 🧠 How the Bloom Filter Works

A **Bloom Filter** is a probabilistic data structure that tests whether an element is part of a set. It can produce false positives but never false negatives, making it highly efficient in terms of space. Each password is hashed multiple times, and the resulting hash positions are used to set corresponding bits in a bit array.

- **Bit Array**: A fixed-size array where each password is mapped to multiple positions via hash functions.
- **Multiple Hashes**: The tool uses **derivative hash functions** to reduce the probability of false positives while minimizing computational overhead. Instead of computing multiple independent hash functions, we derive multiple hashes from just two base hash values, significantly improving performance without sacrificing accuracy.
- **Probabilistic Membership Testing**: The filter may incorrectly indicate that a password is in the dictionary (false positive), but if it says the password is not present, you can be sure it's not.

## 🔧 Future Enhancements

- **Graphical Interface**: Implement a GUI for easier use and real-time feedback.

## 📜 License

This project is licensed under the [MIT License](./LICENSE). - feel free to use and modify it for your own needs.


# Student Management System

A console-based (CLI) Python application for recording, validating, and analyzing student academic data.

## Overview

The program collects student information through an interactive command-line loop, validates every input, calculates grades automatically, and produces a summary report — all without needing a database or external library beyond `rich` for terminal styling.

## Features

- **Input validation for every field**: name (letters only), age (1–120), ID (numeric), class name (alphanumeric), and subject scores (0–100) — each with a retry loop until valid input is given.
- **Automatic grade calculation**: averages three subject scores (Math, English, Science) and assigns a letter grade (A–F) and a Pass/Fail status.
- **Persistent storage**: every student record is appended to a `students.txt` file, so data isn't lost between runs.
- **Batch summary report**: after data entry is finished, the program prints the total number of students, how many passed/failed, full details per student, and identifies the top-performing and weakest student by average score.
- **Repeatable entry loop**: the user can keep entering new students or stop at any time.

## Tech Stack

- **Python 3**
- **[rich](https://github.com/Textualize/rich)** — for styled terminal panels/output

## How It Works

1. Each data field has its own validation function (`Name()`, `Age()`, `ID()`, `Class()`, `Score()`) that loops until the user provides a valid value, printing a clear error message otherwise.
2. `Average()` and `Grade()` turn the three subject scores into a final average and letter grade; `Status()` converts that into Pass/Fail.
3. Each completed student record is stored two ways: appended to an in-memory list (`students`) for the session's summary report, and appended to `students.txt` for persistence across runs.
4. After the user chooses to stop entering students, the program iterates over the in-memory list to compute and print the summary statistics.

## Setup

bash
pip install rich
python Student_Management_System.py

## What I'd Build Next

- Replace the flat text file with a proper database (SQLite) for querying and updating individual records.
- Add edit/delete functionality for existing student records instead of only appending new ones.
- Separate subjects into a configurable list rather than hardcoding Math/English/Science.

---

**Author:** Aramesh Rafiee
[github.com/aramesh-rafiee-dev](https://github.com/aramesh-rafiee-dev) . [linkedin.com/in/aramesh-rafiee-dev](https://www.linkedin.com/in/aramesh-rafiee-dev/).

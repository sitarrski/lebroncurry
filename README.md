# NBA Stats Analyzer: LeBron James vs Stephen Curry

An interactive command-line application built with Python to analyze and visualize historical NBA data. The script evaluates league-wide trends from the modern basketball era (1980-2023) and highlights the career statistics of LeBron James and Stephen Curry.

## Features

* **Interactive CLI Menu:** Choose from 8 different statistical visualizations directly in the terminal.
* **League Trends (1980-2023):** View historical averages for total points per game, 3-point attempts, free-throw percentages, and home vs. away scoring dynamics.
* **Player Profiles:** Track the year-by-year average points (PTS) and assists (AST) for LeBron James and Stephen Curry.
* **Data Processing:** Automatically cleans, filters, and calculates new metrics using `pandas` before visualizing with `matplotlib`.

## Setup

Install the required dependencies:

```bash
pip install pandas matplotlib
```

To run the script, you need to have 3 csv files in the same directory, that are attached to the repository.

## Usage

Run the script from your terminal:

```bash
python project.py
```

You will be presented with menu of various charts to choose from, including (translated from Polish):
1. Average points per game in years 1980-2023
2. Average 3 point attempts in years 1980-2023
3. Average made free throws percentage in years 1980-2023
4. Average points for home vs away teams
5. Points per game for Stephen Curry in years 2009-2023
6. Assists per game for Stephen Curry in years 2009-2023
7. Points per game for LeBron James in years 2003-2023
8. Asissts per game for LeBron James in years 2003-2023
9. Quit

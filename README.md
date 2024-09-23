# Jahnavi Maddhuri: Individual Project 1
This project was originally started for the course, IDS 702: Data Engineering.
The purpose of this project is to provide analysis on a dataset using pandas and Jupyter notebooks in a python project template with a strong build system.
This creates a base feedback loop every time I update my project.

## Directory Tree Structure 
```
JahnaviM-IndividualProject1/
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── .ipynb_checkpoints/
│   └── PandasDescriptiveStatistics-checkpoint.ipynb
├── __pycache__/
│   └── lib.cpython-312.pyc
├── mylib/
│   ├── __pycache__
│       └── lib.cpython-312.pyc
│   └── lib.py
├── Crime_Data_from_2020_to_Present.csv.zip
├── Makefile
├── PandasDescriptiveStatistics.ipynb
├── README.md
├── Summary.md
├── crime_analyze.py
├── requirements.txt
├── test_crime_analyze.py
└──  test_lib.py

```

## CI/CD Badges
[![CI](https://github.com/nogibjj/JahnaviM-MiniProject2/actions/workflows/ex.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-MiniProject2/actions/workflows/ex.yml)
[![FORMAT](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/format.yml) [![INSTALL](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/install.yml) [![LINT](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/lint.yml) [![TEST](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/JahnaviM-IndividualProject1/actions/workflows/test.yml)


## Instructions for Use
To use this repository to generate the analysis, start by cloning the repository. Make sure all the requirements in requirements.txt are fulfilled as these are necessary libraries to run the python script. Finally, run the script, crime_analyze.py, and review the statistics and visualizations. For more information around these insights, look at Summary.md. To see the code and visualizations side by side, look at the Python Notebook, PandasDescriptiveStatistics.ipynb

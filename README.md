# Design Patterns Example Runner

> A collection of Object-Oriented Design Patterns implemented in Python, with a single entry point to run examples.

# Why

In order to write maintainable code, we need structure in our code base. This structure has been mainly standardized into design patterns (OOP).

# What

See https://refactoring.guru/design-patterns

Or book: http://edeleastar.github.io/design-patterns/topic00/pdf/c-logica-gof-catalogue.pdf

# How

Create a Git repository

Use GitFlow to work on the different patterns

# How to Run

## Clone the repository

```
git clone git@github.com:alyn509/reasig-onboarding-design-patterns.git
```

## Create a virtual environment (optional but recommended)

```
python -m venv venv
```

## Activate it:

### On Windows:
```
venv\Scripts\activate
```

### On macOS/Linux:
```
source venv/bin/activate
```

## Install dependencies

```
pip install -r requirements.txt
pip install -e
```

## Run the project

In order to list the available Design Patterns, from the root folder run in terminal

```
python3 -m src.design_patterns_example_runner 
```

If you desire to run the code of a specific design pattern you can add it as an argument to the previous command

```
python3 -m src.design_patterns_example_runner <pattern_name>
```
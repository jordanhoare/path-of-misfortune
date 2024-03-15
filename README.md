# 🤖 Path of Misfortune

- [Introduction](#Introduction)
- [Requirements](#Requirements)
- [Getting Started](#getting-started)

<br>

## ⚡ Introduction
"Path of Misfortune" is a whimsically application designed for Path of Exile players who seek a refreshing twist in their gaming routine. It generates random builds by spinning a series of "wheels of misfortune," selecting an ascendancy and a set of skill gems for you and your friends to challenge yourselves with. Perfect for those adventurous souls who think they've seen it all in Wraeclast and groups looking to add a hefty dose of meme-building fun to their BroSSF league launches.

<br>

## 💻 Requirements

Before starting, ensure you have the following installed:

- [Git](https://git-scm.com/)
- [Poetry](https://python-poetry.org/)
- [Taskfiles](https://taskfile.dev/installation/)
- [Python (3.10+)](https://www.python.org/downloads/)

<br>

## 🚀 Getting Started
To get started with "Path of Misfortune," clone the repository to your local machine and navigate into the project directory:

### Cloning the Repository
To get started with "Path of Misfortune," clone the repository to your local machine and navigate into the project directory:
```zsh
git clone https://github.com/jordanhoare/path-of-misfortune.git
cd path-of-misfortune
```

### Setting up the Environment
Install the project dependencies using Poetry. This will create a virtual environment and install everything needed:

```zsh
poetry install
```

### Running the Application
To launch the "Path of Misfortune" app, use Task to start the Streamlit server. This custom command simplifies the process and ensures consistency across environments:

```zsh
task streamlit:start 
# Alternatively: poetry run streamlit run path_of_misfortune/app.py
```

### Running Code Quality Checks
Run the following command to perform all code quality checks:

```zsh
task code_quality:all
# Alternatively: poetry run ruff --check
```

### Scrape skill gem data
Run the following command to run a bsoup scrap on skill gem data:

```zsh
task scrape:gems
# Alternatively: poetry run python path_of_misfortune/data/scrape_skill_gems.py
```

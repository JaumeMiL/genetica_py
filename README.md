# Genetic Traits Analysis Project 🧬

This repository contains the implementation of a project aimed at analyzing genetic traits using dynamic data structures and object-oriented programming. This project is part of the coursework for the Artificial Intelligence degree at the Universitat Politècnica de Catalunya.

## Authors
- Pablo Abella
- Jaume Mora

## Project Structure 📂
- `main.py` - Main script for running the project.
- `arbre_binari.py` - Implements the genealogical tree structure.
- `conjunt_individus.py` - Manages the set of individuals in an experiment.
- `individu.py` - Stores genetic information of each individual.
- `conjunt_trets.py` - Organizes traits and manages binary tree instances.
- `tret.py` - Manages individuals exhibiting specific traits.
- `cromosoma.py` - Stores information about chromosomes and their intersections.

## Data Analysis 📊
The project starts by simulating genetic experiments involving multiple individuals, each with a pair of chromosomes of fixed length. The genealogical tree is constructed to define the relationships among individuals. The main functionalities of the program include creating experiments, adding traits, querying traits and individuals, and analyzing the distribution of traits within the genealogical tree.

## Main Functionalities
- `experiment`: Initializes a new experiment with specified parameters (number of individuals and genes per chromosome).
- `afegir_tret`: Adds a new trait to a specified individual and updates the combination of genes believed to manifest this trait.
- `consulta_tret`: Queries the combination of genes associated with a specific trait and the individuals that exhibit it.
- `consulta_individu`: Displays information about a specific individual, including their chromosomes and traits.
- `distribucio_tret`: Generates and displays the sub-tree of the genealogical tree that includes all individuals exhibiting a specific trait.
- `fi`: Ends the execution of the program.

## Best Practices 🏆
The project demonstrates efficient handling of genetic data and trait analysis through the use of dynamic data structures and object-oriented programming. Key components include the representation of genealogical trees, management of individuals and their traits, and the analysis of genetic intersections.

## Conclusion 📝
The project highlights the importance of dynamic data structures and object-oriented programming in genetic trait analysis. It provides a robust methodology for managing and analyzing complex genetic data and visualizing genealogical relationships.

## Acknowledgements
- Universitat Politècnica de Catalunya. Grau en Intel·ligència Artificial. Programació i Algorísmia II.

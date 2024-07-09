# RMSD-Calculation-for-Free-Protein-superimposed-to-its-corresponding-DNA-Bound-Structure

## Overview
This Python script calculates the Root Mean Square Deviation (RMSD) between the coordinates of a superimposed free protein structure and its corresponding DNA-bound structure, parsed from a PDB file. The RMSD value provides a measure of structural deviation between the two configurations

### Usage
Input: Ensure that alignedfile_dna_protein.pdb contains the aligned coordinates of the free protein and its DNA-bound structure. Pymol can be employed to align the structures.

Execution: Run the script using Python. It reads the PDB file, extracts atom coordinates for protein (P) and DNA (CA) chains, and calculates RMSD values.

Output: The script prints:
Lengths of protein and DNA coordinate lists.
Mean squared deviation and RMSD values for protein and DNA structures after alignment.

### Notes
- Ensure proper alignment of structures before running the script to obtain accurate RMSD values
- Adjust the script as needed for specific PDB file formats or additional processing requirements

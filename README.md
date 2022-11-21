# Tool for Sequencing Peptides from MS/MS spectra
In the event that one wishes to manually sequence a peptide from a fragmentation spectrum,
the processes is greatly simplified by the use of a difference matrix. Taking the difference
between a list of all the n major peaks (and the parent ion mass) in the 1+ charge state and itself
yields an nxn matrix which can be searched for residue masses. Once the residue masses have been
identified, the process of sequencing simply involves connecting residue masses, alternating between
rows and columns.    
Note: I plan to update this code with an algorithm that will automatically determine the sequence from
the matrix, but for now this must be done manually.
## Example:
Suppose you are given the following spectrum obtained after fragmenting a doubly charged parent ion with 
m/z = 491.26:

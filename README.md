# Tool for Sequencing Peptides from MS/MS spectra
In the event that one wishes to manually sequence a peptide from a fragmentation spectrum,
the processes is greatly simplified by the use of a difference matrix. Taking the difference
between a list of all the n major peaks (and the parent ion mass) in the 1+ charge state and itself
yields an nxn matrix which can be searched for residue masses. Once the residue masses have been
identified, the process of sequencing simply involves connecting residue masses, alternating between
rows and columns.    
Note: I plan to update this code with an algorithm that will automatically determine the sequence from
the matrix, but for now this must be done manually.
## Usage:
`python denovo.py --peaks your_data.csv`
The data should be in the following format:
```
parent
peak_1
peak_2
...
peak_n
```
## Example:
Suppose you are given the following spectrum obtained after fragmenting a doubly charged parent ion with 
m/z = 491.26:  

![mass](https://user-images.githubusercontent.com/47088251/203014639-d0a88c8c-695e-42e4-a16a-859dd620797c.jpg)  

After writing a .csv file with the parent ion mass (singly charged [M+H]) and each major peak, denovo.py was used to generate
a .csv containing the identified residues in the difference matrix. This data was then opened in Excel and used to sequence
the peptide as (L/I)EGFSAVMK.  

![mass2](https://user-images.githubusercontent.com/47088251/203014631-565e5869-4f5e-42b8-9096-aa45f2d63ab6.jpg)

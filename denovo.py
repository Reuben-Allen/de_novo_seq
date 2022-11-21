"""
Author: Reuben Allen
Date: 11/17/2022

This program uses a difference matrix approach to assist in 
de novo peptide sequencing. Given a peak list, this script will
generate a difference matrix and identify amino acid masses within
this matrix. Final sequence requires manual interpretation.
"""

import numpy as np
import argparse

# define dictionary of amino acid masses
amine_dict = {
    "G": 57,
    "A": 71,
    "V": 99,
    "(I/L)": 113,
    "acylC": 160,
    "F": 147,
    "Y": 163,
    "W": 186,
    "S": 87,
    "T": 101,
    "P": 97,
    "(Q/K)": 128,
    "C": 103,
    "M": 131,
    "N": 114,
    "D": 115,
    "E": 129,
    "R": 156,
    "H": 137
    }

# class for calculating difference matrix and identifying aa
class Matrix:
    def __init__(self,peak_list,masses=amine_dict):
        self.masses = masses # dictionary of amino acid masses
        self.peak_list = np.flip(np.sort(peak_list)) # sorted peak list descending

        # initialize difference matrix
        self.diff = np.zeros((self.peak_list.shape[0]+2,self.peak_list.shape[0]+2))
        self.diff[2:,0] = np.subtract(self.peak_list,1) # b-ion start
        self.diff[2:,1] = np.subtract(self.peak_list,19) # y-ion start

        # identified amino acid matrix
        self.aa = np.full(self.diff.shape, "-",dtype=object)
        self.aa[1,0] = "b-start"
        self.aa[0,1] = "b-end"
        self.aa[1,1] = "y-ions"

    def find_residues(self):
        # calculate grid from 1D peak list
        xv,yv = np.meshgrid(self.peak_list,self.peak_list)
        self.diff[2:,2:] = np.abs(np.subtract(yv,xv)) # calculate difference matrix

        # add final amino acids
        self.diff[0,2:] = np.subtract(self.diff[2,2:],18)
        self.diff[1,2:] = self.diff[2,2:]

        # identify residue masses
        rounded_diff = np.round(self.diff) # round to whole number values
        
        # iterate through difference matrix
        for index, i in np.ndenumerate(rounded_diff):
            for key,value in self.masses.items():
                if i == value:
                    self.aa[index[0],index[1]] = key
                else:
                    continue

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Compute and Identify Difference Matrix.')
    parser.add_argument('--peaks', type=str, required=True, help='Full path to .csv file. Each m/z on a separate line.')
    args = parser.parse_args()

    # load data and perform calculations
    peak_list = np.loadtxt(args.peaks,delimiter=",",dtype=np.float64)
    result = Matrix(peak_list)
    result.find_residues()

    # save results
    np.savetxt('denovo_output_residues.csv', result.aa, delimiter = ',',fmt='%s')
    np.savetxt('denovo_output_raw.csv', result.diff, delimiter = ',',fmt='%s')


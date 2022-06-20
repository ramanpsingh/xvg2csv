#!/usr/bin/python

import os, sys
from openpyxl.workbook import Workbook
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Convert a fixed column file to MS Excel and csv file')
parser.add_argument( "-file", type=str, help='File to convert')
parser.add_argument( "-cw", type=int, default=1, help='Option to convert')
args = parser.parse_args()

path=args.file
colwidth=args.cw

# Default filename is the same as that of the xvg file
fn=path[:-4]

# Defines column names for csv and xlsx files
colnames = ["x_%s" %fn, "y_%s" %fn]

if colwidth == 1:
	# Defines column widths in xvg file
	colspecs = [(0, 11), (12, 20)]
	# Reads the xvg file into a DataFrame 
	data = pd.read_fwf(path, colspecs=colspecs, names=colnames)
elif colwidth ==2:
	# Opens the file, reads number of lines and closes the file
	fo=open(path, 'r')
	l=len(fo.readlines())
	fo.close()
	data = pd.read_fwf(path, colspecs='infer', infer_nrows=l, names=colnames)	
else:
	print("Enter a value of 1 or 2 as argument for -cw")

# Writes the DataFrame into csv and xlsx files
data.to_csv("%s.csv" %fn, index=False)
data.to_excel("%s.xlsx" %fn, index=False)

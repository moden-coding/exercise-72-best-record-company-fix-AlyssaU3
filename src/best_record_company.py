#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    records= pd.read_csv("src/UK-top40-1964-1-2.tsv", sep=("\t"))
    
    best= records.groupby("Publisher")["WoC"].sum()
    best_c=best.idxmax()
    mask= records["Publisher"]==best_c
    right_company= records[mask]
    return right_company
def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()

'''
Author: Saideep Gona

Filter small contigs which can cause issues with footprinting and peak calling
'''

from glob import glob
import os
import sys
from os.path import join

chrom_sizes_file = "/project2/lbarreiro/users/Saideep/Rachel_TF_Analysis/ref_genome/sizes.genome"

size_cutoff = 10000

chrom_sizes = {}
with open(chrom_sizes_file, "r") as cs:
    for line in cs:
        p_line = line.strip().split()
        chrom_sizes[p_line[0]] = int(p_line[1])

bed_file = "/project2/lbarreiro/users/Saideep/Rachel_TF_Analysis/longbones_1_longbones_0/footprinting/merged_regions.bed.unfilt"

filtered_out = "/project2/lbarreiro/users/Saideep/Rachel_TF_Analysis/longbones_1_longbones_0/footprinting/merged_regions.bed"

with open(bed_file,"r") as b:
    with open(filtered_out,"w") as o:
        for line in b:
            p_line = line.strip().split()
            if int(p_line[1]) <= 100:
                continue
            if int(p_line[2]) >= (chrom_sizes[p_line[0]]-100):
                continue    
            o.write(line)


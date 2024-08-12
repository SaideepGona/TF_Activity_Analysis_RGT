# TF_Activity_Analysis_RGT
Pipeline used to perform TFT activity analysis using the "RGT" package. Pipeline was used to perform TF activity analysis in the following paper: https://www.nature.com/articles/s41588-024-01668-z .



![alt text](luigi_pipeline/)

## PREREQS (Midway Cluster):

module load python
conda env create <python environment>
conda activate <python environment>
pip install luigi
OR
conda install -c conda-forge luigi
pip install RGT
OR
conda install -c bioconda rgt


## STEPS

1.) Make sure a python environment is created as above, and that the prerequisites are
installed

2.) Create a "metadata" file for the ATACseq alignments. 

    This should be a whitespace delimited table file with the following columns:
    individual_id	condition	bam

    Individual-condition combinations should be unique. If not, please merge files
    ahead of time.

    Where the individual_id is the source of the sample, the condition describes the 
    experimental status of the sample, and bam is the path to the alignment file.

    For activity analysis, the comparison will be done per individual. This means 
    that you should have samples for each condition paired by individual to run the
    analysis.

    templates are provided : example_metadata.(xlsx,txt)

3.) Create a "luigi.cfg" config file (template is provided, example_luigi.cfg) and fill in the
    fields. Place it in a directory of interest (preferablly the output directory)

    This pipeline uses the regulatory genomics toolbox (http://www.regulatory-genomics.org/rgt/basic-introduction/).
    Some config parameters (GENOME,FILTER_PARAMS,MOTIF_DB) are related to RGT.

    REGION_FILES should be a directory of unique bed files containing regions of 
    interest to be analyzed individually.

    NOTE: The config file must specifically be called "luigi.cfg"

5.) Copy the luigi_wrapper.sh file and place it next to the "luigi.cfg" file

6.) To run (with rough runtime estimates):

(long)    bash luigi_wrapper.sh Condition_Footprints --condition1 *Condition1* --condition2 *Condition2*

(short)   bash luigi_wrapper.sh Meta_Footprint --condition1 *Condition1* --condition2 *Condition2*

(short)   bash luigi_wrapper.sh Meta_Motif_Match --condition1 *Condition1* --condition2 *Condition2*
    
    bash luigi_wrapper.sh Enrichment --condition1 *Condition1* --condition2 *Condition2*

        --- AND/OR ---
    
(long)  bash luigi_wrapper.sh Activity --condition1 *Condition1* --condition2 *Condition2*

(short) bash luigi_wrapper.sh Collect_Activity --condition1 *Condition1* --condition2 *Condition2*

    NOTE: Condition1 and Condition2 are conditions from the metadata file to be compared
    in a particular run sequencesqueu

NGS Workshop Excercises
=======================

The purpose of this workshop is to gain experience working with the various file formats discussed in the [NGS file formats lecture](https://github.com/prog4biol/pfb2022/blob/master/workshops/NGS/bio_info_formats.pdf) and the tools designed to manipulate them. We will use real *E. coli* data to perform our analysis: find candidate frameshift mutants in a strain of interest.

**NOTE**: Unless otherwise specified, example command lines are available in this workshop's [lecture notes](https://github.com/bredeson/pfb2022/blob/master/workshops/NGS/bio_info_formats.pdf)

0. First, create a new `ngs` directory for this workshop in which to perform these exercises, then change directory to it.

1. Install the following command line software using [HomeBrew](https://brew.sh) (which is already installed on your workstation):
    ```bash
    brew install wget  # if you don't have it already
    brew install gnuplot
    brew install bwa
    brew install java11
    brew install fastqc
    brew install samtools
    brew install bedtools
    brew install vcftools

    # The following lines are required to run Java-based applications
    echo 'export PATH="/usr/local/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
   

2. Download the Java-based sofware required for this tutorial using `wget`:
    ```bash
    # 1. Fetch each software package .zip archive file:
    wget https://github.com/broadinstitute/gatk/releases/download/4.3.0.0/gatk-4.3.0.0.zip
    wget https://data.broadinstitute.org/igv/projects/downloads/2.14/IGV_2.14.1.zip

    # 2. Unpack each .zip archive:
    unzip filename.zip
    ```


3. Download the [genome](https://raw.githubusercontent.com/prog4biol/pfb2022/master/workshops/NGS/data/Ecoi.fasta.gz) and [annotation](https://raw.githubusercontent.com/prog4biol/pfb2022/master/workshops/NGS/data/Ecoli.gff3.gz) files using `wget`, then decompress them both with `gunzip`.
    - How many of the sequences are chromosomes? How many plasmids?
    - What is the reference strain's genome size?


4. Index the genome as described in the [lecture notes](https://github.com/prog4biol/pfb2022/blob/master/workshops/NGS/bio_info_formats.pdf).


5. Use `wget` to download the FASTQ file of sequencing [reads](https://raw.githubusercontent.com/prog4biol/pfb2022/master/workshops/NGS/data/SRR21901339.fastq.gz) for our strain of interest, then use Unix commands to examine the FASTQ file:
    - How long are the reads?
    - Are these reads single-end or paired-end? Explain how can you tell.
    - Which Phred quality encoding (ASCII offset) are the reads in? How can you tell?


6. Run FastQC on the FASTQ file and examine the report; see `fastqc --help` for a complete list of options. `open` the `fastqc_report.html` to view the report in your browser (you may have to `unzip` the FastQC archive file first). 
    - How many read pairs are in included in the FASTQ file?
    - For which metrics are there warnings?
    - Are there any over-represented sequences in the file? If so, what are they?
    - Are these reads of good quality?


7. Write a python script to trim poor-quality bases from the ends of the FASTQ sequences and output a new FASTQ file. Your script should take as input from the command line: one FASTQ file name and one integer value (the minimum base quality threshold). *HINT*: Use the following approach:
    1. Iterate from the 3'-end of the read to the 5'-end, examining the quality values at each base position (see the [lecture notes](https://github.com/prog4biol/pfb2022/blob/master/workshops/NGS/bio_info_formats.pdf) for how to convert quality string characters to numberic values;  
    2. `break` at the first base with a quality value greater-than or equal-to your inputted quality threshold;  
    3. then use string slicing to extract the high-quality portion of both the sequence and quality strings.  


8. Align the trimmed reads to the genome sequence using BWA-MEM (*i.e.* the `bwa` command). Make sure to specify a Read Group string (via `-R`) that, at a *minimum*, includes `ID`, `SM`, and `PL` tags. This Read Group information is required by GATK. Then, convert the output file to BAM format, sort the BAM file, and then index it (see the [lecture notes](https://github.com/prog4biol/pfb2022/blob/master/workshops/NGS/bio_info_formats.pdf) for how).


9. Run `samtools stats` and `plot-bamstats` on the BAM file and examine the `.html` report.
    - What fraction of reads were mapped to the genome?
    - What is the mode insert size of the sequencing library? Are the read distances reasonably Normally-distributed?
    - Are the majority of reads pairs mapped in inward (FR), outward (RF), or other orientation?
    - Below which base-quality score value does the majority of mismatches occur? Record this value for *Problem 11*.
       >*HINT*: The reads were generated from a strain different from the reference strain and biological SNP differences will also appear in the plot.


10. Use `samtools view` to filter your BAM file to keep alignments with `PAIRED` and `PROPER_PAIR` flags, AND *DO NOT* contain `UNMAP`, `MUNMAP`, `SECONDARY`, `QCFAIL`, `DUP`, or `SUPPLEMENTARY` flags; write the output to a new BAM file and index it.
    > *HINT*: see `samtools flags` for help with flags.


11. Run the GATK HaplotypeCaller to call variants using the final filtered BAM file, set `--min-base-quality-score` to the value you determined in *Step 9*. **NOTE**: Run GATK in the backgound (i.e., `nohup gatk HaplotypeCaller ... &`) or open a second terminal window and work on Problems 12 and 13 while GATK is running in the first.


12. Use the `samtools depth` command to calculate the per-site read depth across the genome (see `samtools depth --help` for more info) and output to a file. The output file will contain three columns: the chromosome name, position (1-based), and read depth. For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    

13. Write a script that computes a text histogram of genomic read depth similar to the example output below (use a `dict` with depth as the key and the count of bases as the value):
    ```
     1 |                                        
     2 |]                                       
     3 |]]                                      
     4 |]]]]]                                   
     5 |]]]]]]]]                                
     6 |]]]]]]]]]]]]]                           
     7 |]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]  
     8 |]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]
     9 |]]]]]]]]]]]]]]]]]]]]]]]]]]]             
    10 |]]]]]]]]]]]]]]]                         
    11 |]]]]]]]]]                               
    12 |]]]]]                                   
    13 |]                                       
    14 |]                                       
    15 |                                        
    ```
    - What is the mean and stdandard deviation of the depth?



14. Use `vcftools` to split the VCF into SNP-specific and InDel-specific files; see `man vcftools` for all available options.
    > *HINT*: You must include `--recode --recode-INFO-all` to output VCF format.


15. Extract CDS features present in `Ecoli.gff3` and create a new GFF3 file, then use `bedtools intersect` to determine:
    - How many SNPs and InDels intersect these CDS features?
    - How many InDels might cause frameshifts? (Write a script)



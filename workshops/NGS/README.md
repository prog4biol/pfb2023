NGS File Types Workshop Excercises
=======================

The purpose of this workshop is to gain experience working with the various file formats discussed in the [NGS file formats lecture](bio_info_formats.pdf) and the tools designed to manipulate them. We will use real *E. coli* data to perform our analysis: find candidate frameshift mutants in a strain of interest.

**NOTE**: Unless otherwise specified, example command lines are available in this workshop's [lecture notes](bio_info_formats.pdf)

1. First, create a new `ngs` directory for this workshop in which to perform these exercises, then change directory to it.

2. Install the following command line software using Miniconda. If you haven't already, use the instructions to install Miniconda detailed in the [Biopython problemset](../../problemsets/biopython_problemset.md).
    ```bash
    # add channels to download tools from:
    $ conda config --add channels defaults
    $ conda config --add channels conda-forge
    $ conda config --add channels bioconda

    # create an environment and activate it
    $ conda create --name ngs
    $ conda activate ngs

    # Install tools for analysis
    $ conda install wget gnuplot
    $ conda install -c bioconda bwa fastqc samtools bcftools bedtools 
    ```
   

3. Download the Java-based sofware required for this tutorial using `wget`:
    ```bash
    # 1. Fetch each software package .zip archive file:
    $ wget https://github.com/broadinstitute/gatk/releases/download/4.3.0.0/gatk-4.3.0.0.zip

    # 2. Unpack the .zip archive:
    $ unzip gatk-4.3.0.0.zip
    ```


4. Download the following genome files with `wget`, then decompress both with `gunzip`:
    ```bash
    # Genome sequence:
    $ wget https://github.com/prog4biol/pfb2023/raw/master/workshops/NGS/data/Ecoli.fasta.gz

    # Genome annotation:
    $ wget https://raw.githubusercontent.com/prog4biol/pfb2023/master/workshops/NGS/data/Ecoli.gff3.gz
    ```
    - Use the _E. coli_ FASTA file to determine how many of the sequences are chromosomes? How many plasmids?
    - Use the _E. coli_ FASTA file to determine the genome size?


5. Index the genome to make it quickly searchable by BWA, GATK, and other tools.
    ```bash
    $ samtools faidx Ecoli.fasta
    $ samtools dict Ecoli.fasta >Ecoli.dict
    $ bwa index Ecoli.fasta
    ```


6. Use `wget` to download the FASTQ file of sequencing [reads](data/SRR21901339.fastq.gz) for our strain of interest, then use Unix commands to examine the FASTQ file:
    ```
    # Whole-genome sequnecing reads:
    $ wget https://github.com/prog4biol/pfb2023/raw/master/workshops/NGS/data/SRR21901339.fastq.gz

    $ gunzip SRR21901339.fastq.gz
    ```
    - How long are the reads? (hint: you can use `head`, `tail`, and `wc`)
    - Are these reads single-end or paired-end? Explain how can you tell. 
    - Which Phred quality encoding (ASCII offset) are the reads in? How can you tell?


7. Run FastQC on the FASTQ file and examine the report; see `fastqc --help` for a complete list of options. `open` the `fastqc_report.html` to view the report in your browser (you may have to `unzip` the FastQC archive file first). 
    - How many read pairs are in included in the FASTQ file?
    - For which metrics are there warnings?
    - Are there any over-represented sequences in the file? If so, what are they?
    - Are these reads of good quality?


8. Write a python script to trim poor-quality bases from the ends of the FASTQ sequences and output a new FASTQ file and output the trimmed reads to a file named `SRR21901339.trim.fastq`. Your script should take as input from the command line: one FASTQ file name and one integer value (the minimum base quality threshold). *HINT*: Use the following approach:
    1. Iterate from the 3'-end of the read to the 5'-end, examining the quality values at each base position (see the [lecture notes](bio_info_formats.pdf) for how to convert quality string characters to numberic values;  
    2. `break` at the first base with a quality value greater-than or equal-to your inputted quality threshold;  
    3. then use string slicing to extract the high-quality portion of both the sequence and quality strings.  


9. Align the trimmed reads to the genome sequence using BWA-MEM (*i.e.* the `bwa` command). Make sure to specify a Read Group string (via `-R`) that, at a *minimum*, includes `ID`, `SM`, and `PL` tags. This Read Group information is required by GATK. Then, convert the output file to BAM format, sort the BAM file, and then index it (see the [lecture notes](bio_info_formats.pdf) for how).
    ```bash
    # use BWA's MEM algorithm to align reads to the genome as paired-ends:
    $ bwa mem -Mp -t4 -R '@RG\tID:SRR21901339\tSM:Ecoli\tPL:ILLUMINA' Ecoli.fasta SRR21901339.trim.fastq | samtools view -b - >SRR21901339.bam

    # sort the alignments by genomic coordinates:
    $ samtools sort -m 1g -o SRR21901339.srt.bam SRR21901339.bam

    # index the sorted alignments:
    $ samtools index SRR21901339.srt.bam
    ```


10. Run `samtools stats` and `plot-bamstats` on the BAM file and examine the `.html` report.
    ```bash
    $ samtools stats --ref-seq Ecoli.fasta SRR21901339.srt.bam >SRR21901339.stats
    $ plot-bamstats -s Ecoli.fasta >Ecoli.gc
    $ plot-bamstats -r Ecoli.gc -p SRR21901339 SRR21901339.stats

    # Finally, open the output HTML file in your web Safari browser:
    $ open -a Safari.app SRR21901339.html
    ```
    - What fraction of reads were mapped to the genome?
    - What is the mode insert size of the sequencing library? Are the read distances reasonably Normally-distributed?
    - Are the majority of reads pairs mapped in inward (FR), outward (RF), or other orientation?
    - Below which base-quality score value does the majority of mismatches occur? Record this value for *Problem 11*.
       >*HINT*: The reads were generated from a strain different from the reference strain and biological SNP differences will also appear in the plot.


11. Use `samtools view` to filter your BAM file to keep alignments with `PAIRED` and `PROPER_PAIR` flags, AND *DO NOT* contain `UNMAP`, `MUNMAP`, `SECONDARY`, `QCFAIL`, `DUP`, or `SUPPLEMENTARY` flags; write the output to a new BAM file and index it. What fraction of the reads are properly paired?
    ```bash
    # Get the SAM flags for properly-paired reads, do:
    $ samtools flags PAIRED,PROPER_PAIR
    0x3	     3	   PAIRED,PROPER_PAIR

    # Get the SAM flags value to exclude poor quality data:
    $ samtools flags UNMAP,MUNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY
    0xf0c	3852	UNMAP,MUNMAP,SECONDARY,QCFAIL,DUP,SUPPLEMENTARY

    # Then filter reads with `samtools view` to output to a new BAM
    # file, selecting _for_ reads that are properly-paired and
    # _removing_ the poor-quality reads:
    $ samtools view -b -f3 -F3852 SRR21901339.srt.bam >SRR21901339.proper.bam

    # Now, index the new BAM file:
    $ samtools index SRR21901339.proper.bam
    ```
    > *HINT*: see `samtools flags` for help with flags.


12. Run the GATK HaplotypeCaller to call variants using the final filtered BAM file, set `--min-base-quality-score` to the value you determined in *Step 9*. **NOTE**: Run GATK in the backgound (i.e., `nohup gatk HaplotypeCaller ... &`) or open a second terminal window and work on Problems 13 and 14 while GATK is running in the first.
    ```bash
    ./gatk-4.3.0.0/gatk HaplotypeCaller \
         --minimum-mapping-quality 30 \
         --min-base-quality-score 30 \
         --read-validation-stringency SILENT \
         --reference Ecoli.fasta \
         --input SRR21901339.proper.bam \
         --output SRR21901339.vcf
    ```


13. Use the `samtools depth` command to calculate the per-site read depth across the genome (see `samtools depth --help` for more info) and output to a file. The output file will contain three columns: the chromosome name, position (1-based), and read depth. For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    

14. Write a python script that computes the genome-wide [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) read depth parameters.


15. Using command-line tools, extract CDS features present in `Ecoli.gff3` and create a new GFF3 file. Then use `bedtools intersect` to determine how many SNPs and InDels in the VCF file intersect these CDS features.


16. Compress the VCF with `bgzip`, then index it with `bcftools index --tbi your.vcf.gz`.


17. Calculate variant consequence using the `bcftools csq` tool (inputting `Ecoli.gff3` and *not* the CDS-specific GFF3) and output to a new VCF file. Then, write a python script to parse variant consequence annotations from the INFO BCSQ tag and calculate the [Z-score](https://en.wikipedia.org/wiki/Standard_score) from the Sample DP field in this new VCF, then output this information into a tab-delimited file summarizing the framehift variants. Use the mean and standard deviation parameters calculated in Problem 14 as inputs to your script to calculate the Z-score.
    - How many variants induce frameshifts?
    - How many frameshifts cause stop codons to be lost? How many gained?
    - How many of these frameshift variants have a read depth Z-scores between -2 and +2?
    - Why might we be skeptical of variants with very low or very high read depths?

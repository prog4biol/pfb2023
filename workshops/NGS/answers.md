NGS File Types Workshop Excercises
=======================

The purpose of this workshop is to gain experience working with the various file formats discussed in the [NGS file formats lecture](bio_info_formats.pdf) and the tools designed to manipulate them. We will use real *E. coli* data to perform our analysis: find candidate frameshift mutants in a strain of interest.

**NOTE**: Unless otherwise specified, example command lines are available in this workshop's [lecture notes](bio_info_formats.pdf)

1. First, create a new `ngs` directory for this workshop in which to perform these exercises, then change directory to it.
    **ANSWER**:
    ```bash
    $ mkdir ngs; cd ngs
    ```

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
    
	**ANSWER**: Illumina reads come off the sequencer all the same length, so we only need count the first.
        - `head -n 2` will return the first two lines in the file, which we pipe as input to `tail`
        - `tail -n 1` then returns just the sequence line, which we pipe as input to `wc`
        - `wc -L` returns the length of the line (using `wc -c` counts the number of characters (including the terminal `\n`)
	```bash
	$ head -n 2 SRR21901339.fastq | tail -n 1 | wc -L
	# returns: 149
	```

    - Are these reads single-end or paired-end? Explain how can you tell.
    
        **ANSWER**: The following command uses a pattern anchored to the beginning of the line, searching for the character that begins the sequence header for each record (WARNING: in low-quality datasets, these characters can also appear at the beginning of quality strings).
        - `grep '^@'` will return sequence headers (they all begin with the @ char), which we pipe as input to `head`
        - `head` will truncate our input to the top 10 (by default) lines only.  
        ```bash
	$ grep '^@' SRR21901339.fastq | head
	# returns:
	@1/1
	@1/2
	@2/1
	@2/2
	@3/1
	@3/2
	@4/1
	@4/2
	@5/1
	@5/2
	```
	Our FASTQ file contains paired-end reads because there are consecutive pairs of reads with identical IDs (the part of the read name after `@` and upto, but not including, the `/`) and the end number is indicated by `/1` and `/2` for first and second mates, respectively.
	
    - Which Phred quality encoding (ASCII offset) are the reads in? How can you tell?
    
        ANSWER: This problem requires you to view the FASTQ file using a tool like `more` or `less` to scan through the file and examine a few quality strings. The idea is to look for characters that occur outside one Phred offset system or the other to narrow down which system is being used. One can quickly translate characters to their decimal values by referencing this [Encoding](https://en.wikipedia.org/wiki/FASTQ_format#Encoding) figure). For example, the `SRR21901339.fastq` file contains the `/` character in the first read quality line, which is included in the Phred 33 encoding, but not other Phred encodings.
    

7. Run FastQC on the FASTQ file and examine the report; see `fastqc --help` for a complete list of options. `open` the `fastqc_report.html` to view the report in your browser (you may have to `unzip` the FastQC archive file first).
    - How many read pairs are in included in the FASTQ file?
        **ANSWER**: On the Unix command-line on a Mac, you can run the following command to open an HTML file in your web browser using the following command:
	```bash
	$ unzip SRR21901339_fastqc.zip
	$ open -a Safari.app SRR21901339_fastqc/fastqc_report.html
	```
	In the "Basic Statistics" table and "Total Sequences" row, there are 400000 sequences, and since we determined the reads are paired, there are 200000 pairs.
	
    - For which metrics are there warnings?
        **ANSWER**: In the left-side pane, the "Per base sequence content" and "Per sequence GC content" metrics show a failure and warning, respectively. The "Per base sequence content" is erratic in the first 12 (or so) bases, which is pretty normal for Illumina datasets (particularly if the reads were barcoded/multiplexed). The "Per sequence GC content" is a warning because of the slightly heavy left/lower shoulder, but is otherwise unimodal and fairly Normally-distributed.
	
    - Are there any over-represented sequences in the file? If so, what are they?
        **ANSWER**: The Nextera Transposase Sequence is slightly elevated, but the "Overrepresented sequences" metric (left-side pane) doesn't indicate a failure. Either way, it would be best-practice to trim Nextera Transposase adapter sequences from the reads.

    - Are these reads of good quality?
        **ANSWER**: Yes, mostly, the reads pass most metrics; the per-base sequence qualities are really good, the per base N content is near-zero, per base sequence content shows no obvious bias after the 15th position, and duplication levels and contaminant levels are low.


8. Write a python script to trim poor-quality bases from the ends of the FASTQ sequences and output a new FASTQ file and output the trimmed reads to a file named `SRR21901339.trim.fastq`. Your script should take as input from the command line: one FASTQ file name and one integer value (the minimum base quality threshold). *HINT*: Use the following approach:
    1. Iterate from the 3'-end of the read to the 5'-end, examining the quality values at each base position (see the [lecture notes](bio_info_formats.pdf) for how to convert quality string characters to numberic values;  
    2. `break` at the first base with a quality value greater-than or equal-to your inputted quality threshold;  
    3. then use string slicing to extract the high-quality portion of both the sequence and quality strings.  
    **ANSWER**: See the source code [here](https://github.com/prog4biol/pfb2023/raw/master/workshops/NGS/answers/trim-read-qualities.py) for the `trim-read-qualities.py` script for the solution to this problem.
    ```bash
    # Add execute permissions:
    $ chmod +x ./trim-read-qualities.py

    # Run the script and trim reads:
    $ ./trim-read-qualities.py SRR21901339.fastq 28 >SRR21901339.trim.fastq
    ```

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
      **ANSWER**: In the lower left panel, under the "Reads" section, the "mapped" metric should show approximately 342,550 (85.6%).
      
    - What is the mode insert size of the sequencing library? Are the read distances reasonably Normally-distributed?
      **ANSWER**: The top left plot ("Insert size") shows the insert size of templates stratified into "inward" or "outward" -oriented read pairs. The insert size is ~274 bp.
      
    - Are the majority of reads pairs mapped in inward (FR), outward (RF), or other orientation?
      **ANSWER**: When aligning reads with BWA-MEM, it reports the estimated numbers of read pairs in the four possible orientations: forward-forward (FF), forward-reverse (FR), reverse-forward (RF), and reverse-reverse (RR). The vast majority are in FR orientation.
      ```bash
      $ bwa mem -Mp -t4 -R '@RG\tID:SRR21901339\tSM:Ecoli\tPL:ILLUMINA' Ecoli.fasta SRR21901339.trim.fastq | samtools view -b - >SRR21901339.bam
      [M::bwa_idx_load_from_disk] read 0 ALT contigs
      [M::process] read 272308 sequences (40000042 bp)...
      [M::process] 0 single-end sequences; 272308 paired-end sequences
      [M::process] read 127692 sequences (18728620 bp)...
      [M::mem_pestat] # candidate unique pairs for (FF, FR, RF, RR): (262, 110626, 21, 222) <===== HERE
      [M::mem_pestat] analyzing insert size distribution for orientation FF...
      [M::mem_pestat] (25, 50, 75) percentile: (288, 570, 1203)
      [M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 3033)
      [M::mem_pestat] mean and std.dev: (686.12, 591.39)
      [M::mem_pestat] low and high boundaries for proper pairs: (1, 3948)
      [M::mem_pestat] analyzing insert size distribution for orientation FR...
      [M::mem_pestat] (25, 50, 75) percentile: (237, 307, 391)
      [M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 699)
      [M::mem_pestat] mean and std.dev: (316.76, 118.06)  
      [M::mem_pestat] low and high boundaries for proper pairs: (1, 853)
      [M::mem_pestat] analyzing insert size distribution for orientation RF...
      [M::mem_pestat] (25, 50, 75) percentile: (40, 83, 152)
      [M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 376)
      [M::mem_pestat] mean and std.dev: (103.38, 85.18)
      [M::mem_pestat] low and high boundaries for proper pairs: (1, 488)
      [M::mem_pestat] analyzing insert size distribution for orientation RR...
      [M::mem_pestat] (25, 50, 75) percentile: (312, 503, 966)
      [M::mem_pestat] low and high boundaries for computing mean and std.dev: (1, 2274)
      [M::mem_pestat] mean and std.dev: (563.66, 405.17)
      [M::mem_pestat] low and high boundaries for proper pairs: (1, 2928)
      ```

    - Below which base-quality score value does the majority of mismatches occur? Record this value for *Problem 12*.
       >*HINT*: The reads were generated from a strain different from the reference strain and biological SNP differences will also appear in the plot.
       **ANSWER**: The left-most plot on the second row is the "Mismatches per cycle" plot, showing the number of mismatches (relative to the reference) per read position. The majority of mismatches are in the high-quality 30+ base-quality, but the absolute number of differences *decreases* near the 3' ends of the reads, so these are the biological SNP differences. The majority of basecall error-derived differences are in the base quality < 20 regime, as they *increase* closer to the 3' end.


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
    **ANSWER**: We can use flags to count the number of properly-paired read pairs by counting just the R1 reads, as for a pair to be properly paired, both ends need to be mapped (no unmapped R2 reads). The `-f 64` flag selects for reads with the READ1 bit flag set. The fraction is: 167346 / 201250 (83.2%):
    ```bash
    $ samtools view -f 64 SRR21901339.srt.bam | wc -l
    201250
    $ samtools view -f 64 SRR21901339.proper.bam | wc -l
    167346
    ```

12. Run the GATK HaplotypeCaller to call variants using the final filtered BAM file, set `--min-base-quality-score` to the value you determined in *Step 10*. **NOTE**: Run GATK in the backgound (i.e., `nohup gatk HaplotypeCaller ... &`) or open a second terminal window and work on Problems 13 and 14 while GATK is running in the first.
    ```bash
    $ nohup ./gatk-4.3.0.0/gatk HaplotypeCaller \
         --minimum-mapping-quality 30 \
	 --min-base-quality-score 20 \
         --read-validation-stringency SILENT \
         --reference Ecoli.fasta \
         --input SRR21901339.proper.bam \
         --output SRR21901339.vcf &
    ```


13. Use the `samtools depth` command to calculate the per-site read depth across the genome (see `samtools depth --help` for more info) and output to a file. The output file will contain three columns: the chromosome name, position (1-based), and read depth. For example:
    ```
    chrI	1	15
    chrI	2	15
    chrI	3	14
    chrI	4	16
    chrI	5	16
    ```
    **ANSWER**: If you call variants using a specific set of minimum mapping quality and base quality thresholds, use the same thresholds when calculating depth.
    ```bash
    $ samtools depth -q20 -Q30 SRR21901339.proper.bam >SRR21901339.proper.depth
    ```
    

14. Write a python script that computes the genome-wide [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) read depth parameters.
    **ANSWER**: See the source code [here](https://github.com/prog4biol/pfb2023/raw/master/workshops/NGS/answers/calc-summary-stats.py) for the `calc-summary-stats.py` script for the solution to this problem.
    ```bash
    # Run the script like so:
    $ ./calc-summary-stats.py SRR21901339.proper.depth
    filename	mean	sd
    SRR21901339.proper.depth	10.69	4.31
    ```


15. Using command-line tools, extract CDS features present in `Ecoli.gff3` and create a new GFF3 file. Then use `bedtools intersect` to determine how many SNPs and InDels in the VCF file intersect these CDS features.
    ```bash
    # First, pull out CDS features, including the GFF3 header,
    # using multiple patterns/expressions (-e):
    $ grep -e '^#' -e 'CDS' Ecoli.gff3 >Ecoli.cds.gff3

    # calculate the number of SNPs+InDels in the CDS regions:
    $ bedtools intersect -u -a SRR21901339.vcf -b Ecoli.cds.gff3 | wc -l
    88005
    ```


16. Compress the VCF with `bgzip`, then index it with `bcftools index --tbi your.vcf.gz`.
    **ANSWER**:
    ```bash
    $ bgzip SRR21901339.vcf
    $ bcftools index --tbi SRR21901339.vcf.gz
    ```


17. Calculate variant consequence using the `bcftools csq` tool (inputting `Ecoli.gff3` and *not* the CDS-specific GFF3) and output to a new VCF file. Then, write a python script to parse variant consequence annotations from the INFO BCSQ tag and calculate the [Z-score](https://en.wikipedia.org/wiki/Standard_score) from the Sample DP field in this new VCF, then output this information into a tab-delimited file summarizing the framehift variants. Use the mean and standard deviation parameters calculated in Problem 14 as inputs to your script to calculate the Z-score.
    **ANSWER**:
    ```bash
    # If you try running bcftools csq and get a warning about unphase heterozygous variants,
    # include the `--phase s` option to skip them (E. coli is haploid):
    $ bcftools csq --phase s --fasta-ref Ecoli.fasta --gff-annot Ecoli.gff3 SRR21901339.vcf.gz >SRR21901339.csq.vcf

    # Now, run our script to output a table of frameshift variants with Z-score:
    $ extract-csq-info.py SRR21901339.csq.vcf 10.69 4.31 >SRR21901339.csq.tsv
    ```
    - How many variants induce frameshifts? **ANSWER**:
        ```bash
	$ grep -c frameshift
	72
	```

    - How many frameshifts cause stop codons to be lost? How many gained?
        ```bash
	$ grep -c stop_gained SRR21901339.csq.tsv
	9
	
	$ grep -c stop_lost SRR21901339.csq.tsv
	6
	```

    - How many of these frameshift variants have a read depth Z-scores between -2 and +2?
        **ANSWER**: There should be 11 frameshift variants with Z-score < -2, none > 2.
        ```bash
	# Sort on the Z-score column and examine the values:
	$ sort -k3,3g SRR21901339.csq.tsv | less -S  # count them up
	```

    - Why might we be skeptical of variants with very low or very high read depths?
        **ANSWER**: Variants at very low read depth may be called in regions of the genome that are difficult to map; the genome may be repetitive or there is a complex structural difference between the two genomes that makes mapping short reads from one genome to the other difficult. Variants at very high read depth are likely also derived from or mapping to repeats, where the genome from which the reads were sampled may contain more copies of a particular repeat than the reference (biological copy-number variant), or the repeats in the reference genome are collapsed (genome assembly error).


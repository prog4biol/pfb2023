# Genome Assembly Workshop

Lecture Notes: See [PDF](Triant_GenomeAssembly_PFB_2023.pdf)  
Workshop Notes: See [PDF](Triant_AssemblyWorkshop_PFB2023.pdf)


# Problem Set

## Exercise 1: Genome Stats

Using [ecoli-0.25.contigs.fasta](ecoli_0.25.contigs.fasta), write a script that reports:

1. The number of contigs in the file
2. The shortest contig.
3. The longest contig.
4. Total contig length.
5. The L50 size
6. The N50 size

## Exercise 2: Soft repeat-masked genome

When running RepeatMasker or other software that identifies repetitive sequences in a genome, the resulting sequence can be “soft-masked”. This means that the nucleotides that are contained in repetitive elements are in lower-case letters. Any gaps present in the genome, where the sequence is unresolved are marked with ”N”s.

**NNNNNNNNNNNN**CAGCAAAGACAAA**caaacaaatatacaaagac**AAAAATTGCCACAGCAAAGACAAAGAGATAAATAAAAGGCACAAAATTGTCAC

For the following exercise, write a python script that parses a FASTA file, _D. melanogaster_ chromosome assembly, and identify the following:
 1. How many contigs?
 2. Nucleotide content:
    - number of each nucleotide both masked (a,c,g,t) and not (A,C,G,T)
 3. What proportion of the genome is comprised of gaps?

The fasta file for the exercise: 
[D_melanogaster_genomic.fna](D_melanogaster_genomic.fna)





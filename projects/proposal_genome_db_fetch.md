# Genome database fetch tool

## Description of problem
Databases (DBs) such as NCBI, EMBL-EBI, and Phytozome use standardized and predictable URLs for accessing genome resources (genome sequences and annotations). However, there is presently no one unifying client-side Python API to download and reformat genome sequences and their annotations from these DBs. Such a tool could be used to ease the data retrieval process (especially when downloading many genomes) and be incorporated into large analysis pipelines, thereby enhancing reproducibility.

## Proposed programming solution

The proposal for this project is to implement a Python API to query and fetch genome sequences and annotations from NCBI, EMBL-EBI, DDBJ, Phytozome, and/or other large resource providers. Becuase these large DBs often assign their own unique identifers to each sequence, it's often necessary to convert the NCBI/EMBL-EBI/DDJB/other database-native identifiers (e.g., NC_000001.11 or CM000663.2) back to their original, submitted identifiers (e.g., chr1). This API can be further extended to automatically index genomes and generate CDS and peptide sequences from downloaded GFF3s. A Python program using the API could also be written to allow access to these tools via the command-line.

## Overview of features/stages/components to be implemented
### How the proposed code solves the problem
The API will provide a set of programming classes/functions to abstract the data retrieval process. The code specific to retrieving data from each DB can be wrapped in a DB-specific module, which is accessed by providing the DB and a genome identifier, for example:

```python
# The user calls a generic entry-point module/class function:
database = GenomeDB.get("NCBI", "GCF_000001405.40")

# which, further delegates to the appropriate database-specific class/function:
return GenomeDB.NCBI.get("GCF_000001405.40")
```

The DB-specific module can then re-code the sequence identifiers in both FASTA and GFF3 files, as appropriate, eliminating the need for the API user to perform this task explicitly.

If specified by the user, annotated gene sequences (such as CDS and peptides) can be outputted to file using a single function call made by main API layer.

Because of the number of databases and possible functionality (sequence identifier re-coding, extracting CDS sequences and translating peptides), the code base can be readily broken down into multiple independent components (modules) that multiple developers can write simultaneously.

### Desired inputs

1. A database name (e.g., "NCBI")
2. A genome identifier (e.g., "GCF_000001405.40")
3. Optional arguments to specify whether to export CDS and peptide sequences from the annotation GFF3. The translation table may also need to be specified.

### Desired outputs

1. Fetch from the specified database the genome sequences in FASTA format, and annotations in GFF3 format, and organize with a standardized file hierarchy.  
2. As needed, fetch the sequence identifier mapping table (e.g., NCBI `assembly_report.txt` file) to re-code the sequence identifiers.  
3. Main API class returns an object containing the FASTA and GFF3 file paths that can be used to open and read those files, for example:  
    ```python
    GenomeDBinstance.genome_fasta_filepath  # returns the file path to the genome sequences
    GenomeDBinstance.genome_annotation_filepath  # return the file path to the genome annotations
    GenomeDBinstance.cds_sequence_filepath  # returns the file path to the CDS sequences
    GenomeDBinstance.peptide_sequence_filepath  # returns the file path to the translated CDS peptides
    ```
## Potential challenges that may be encountered
Some data portals (such as Phytozome) require a user name and password; requiring potentially writing in authentication interfaces to access data from such portals.

## Anticipated programming concepts (logic, data structures, modules, algorithms, etc.) to be used in implementing the solution

- Due to the modular nature of this API, modules and classes are the most appropriate data structures to implment this.
- The main, abstracted API layer will need to choose from a given set of supported databases to determine call the appropriate database-specific API sublayer (using conditional statements).
- File downloads can performed using calls to Unix tools (e.g., `curl`) or use public Python libraries (using the `subprocess` or `http` modules, respectively).
- Modules extracting CDS and peptide sequences to file will require FASTA and GFF parsing: specifically file IO, string operations, and likely dictionaries).

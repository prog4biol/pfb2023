# genAI - Programming for Biology

chatGPT and writing code 

here's the prompt

```
write a python script to run blast on a series of fasta files with names matching 'data*.fa'. The script should run the blasts in the background and wait for them all to finish
```



here's a script

```python
import subprocess
import glob
import os

def run_blast(fasta_file):
    # Define BLAST command
    blast_cmd = [
        'blastn',               # Use blastn for nucleotide sequences; change if needed
        '-query', fasta_file,   # Input FASTA file
        '-db', 'nt',            # BLAST database to use; change if needed
        '-out', f'{fasta_file}.blast.out',  # Output file
        '-outfmt', '6',         # Output format
        '-num_threads', '4',    # Number of threads to use; change if needed
        '-evalue', '1e-5',      # E-value threshold; change if needed
        '-max_target_seqs', '10'  # Maximum number of target sequences to report; change if needed
    ]
    
    # Run BLAST command in the background
    subprocess.Popen(blast_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"BLAST started for {fasta_file}")

def main():
    # Find all FASTA files matching 'data*.fa'
    fasta_files = glob.glob('data*.fa')
    
    # Check if any FASTA files found
    if not fasta_files:
        print("No FASTA files found matching 'data*.fa'")
        return
    
    # Run BLAST for each FASTA file
    processes = []
    for fasta_file in fasta_files:
        # Run BLAST in the background
        process = subprocess.Popen(['blastn', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        
        if "blastn" in out.decode():
            run_blast(fasta_file)
        else:
            print("BLAST not found. Make sure BLAST executables are in your PATH.")
            return
    
    # Wait for all BLAST processes to finish
    for process in processes:
        process.wait()

    print("All BLAST processes have finished.")

if __name__ == "__main__":
    main()

```

run it like so

```
~/projects/chatGPT/supposedToRunParallelBlastJobs.py 
BLAST started for BB_ONT7_smpl6.inclUMI.slop=4.extracted.fa
BLAST started for BB_ONT7_smpl5.flanks.slop=4.extracted.fa
BLAST started for BB_ONT7_smpl5.inclUMI.slop=4.extracted.fa
BLAST started for BB_ONT7_smpl6.flanks.slop=4.extracted.fa
All BLAST processes have finished.
```

Hmmm. 



Better script

```python
#!/usr/bin/env python3
# actually does run blast jobs in parallel and wait until done.
# checks for failed blast jobs and exits.


import subprocess
import glob
#import os
import sys

prefix=sys.argv[1] or ''
db = sys.argv[2] or 'nt'


def run_blast(fasta_file):
    # Define BLAST command
    blast_cmd = [
        'blastn',               # Use blastn for nucleotide sequences; change if needed
        '-query', fasta_file,   # Input FASTA file
        '-db', db,            # BLAST database to use; change if needed
        '-out', f'{fasta_file}.blast.out',  # Output file
        '-outfmt', '6',         # Output format
        '-num_threads', '3',    # Number of threads to use; change if needed
        '-evalue', '1e-5',      # E-value threshold; change if needed
        '-max_target_seqs', '10'  # Maximum number of target sequences to report; change if needed
    ]
    
    # Run BLAST command in the background
    process = subprocess.Popen(blast_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # don't use this
    # out, err = process.communicate()  # waits until finished
    return process

    print(f"BLAST started for {fasta_file}")

def main():
    # Find all FASTA files matching 'data*.fa'
    fasta_files = glob.glob('BB*.fa')
    
    # Check if any FASTA files found
    if not fasta_files:
        print("No FASTA files found matching 'data*.fa'")
        return
    
    # check blast can be run
    process = subprocess.Popen(['blastn', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if not "blastn" in out.decode():        
        print("BLAST not found. Make sure BLAST executables are in your PATH.")
        exit(1)
    
    
    # Run BLAST for each FASTA file
    processes = []
    for fasta_file in fasta_files:
        # Run BLAST in the background    
        process = run_blast(fasta_file)
        processes.append(process)

    # Wait for all BLAST processes to finish
    for process in processes:
        ret = process.wait()  # sets returncode. Need to check this is zero!!!
        if ret != 0:
            print(f"BLAST process failed with return code {ret}")
            exit(1)

    print("All BLAST processes have finished.")

if __name__ == "__main__":
    main()

```


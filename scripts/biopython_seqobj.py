#!/usr/bin/env python3
import Bio.Seq                          
seqobj = Bio.Seq.Seq('ATGCGATCGAGC')     
print(f"{seqobj} has {len(seqobj)} nucleotides")

Interproscan PTHR2GO
====================


We have a gene list we created for stem cell proliferation genes in alpaca. Let's look at these genes and see if there are any reoccurring GO terms or PFAM domains in our gene set.


Generate a FASTA file to use to predict protein domains and motifs using InterProScan. 




__Create FASTA for stem cell proliferation genes:__

1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/3e66a7a80107043f1317566a8a10fed1).
2. In dropdown box, select "Ensembl Genes 110"  (or most current version)
3. In dropdown box, select "Alpaca Genes" 
4. On the left, click Attributes
5. Expand GENE:
6. Deselect "transcript stable ID", "Gene stable ID version", and "transcript stable ID version".
7. These should be selected: Gene stable ID, Gene name, Gene description
8. Click Results (top left)
9. Click "Filters"
10. Under "Gene Ontology", check "Go term name" and enter "stem cell proliferation" (clear out any previous GO term names)
11. Click Attributes (left menu)
12. Then click the (o) for "Sequences" in the list of options near the top (Features, Homologues, Structures, Sequences)
13. In the SEQUENCES box make sure 'Peptide' is selected
14. Click Results (top left)
15. Export all results to "File" "FASTA" --> GO
16. Rename the file to "alpaca_stemcellproliferation_genes.fa"

__Predict Protein domains and motifs__

1. Go to there InterProScan Server:
2. https://www.ebi.ac.uk/interpro/search/sequence/
3. Paste in your stem cell proliferation FASTA file. "alpaca_stemcellproliferation_genes.fa"
4. Click the Automatic FASTA clean button. We have *s in our file for stop codons, InterProScan does not like those.
5. Once the search is complete, Click 'Group Actions' then Download All. You will get a json file that is named similar to this: 20231021-172942-29.json
6. Parse the downloaded json file. Use the PANTR2GO mappings to see if there is a recurring GO term in our stem cell proliferation gene list. You can try this from scratch or use my script and fill in a few keys to get the GO terms. 
7. See if there is a PFAM domain that is recurring in our stem cell proliferation gene list. You can try this from scratch or use my script and fill in a few keys to get the PFAM domain hits. 
8. If you finish the all the other questions, look through your IPRSCAN results to pick another type of domain hit to add to your parser in a similar format to PFAM domains.



Here is example of the JSON 2 Python datastructure that the PTHR and PFAM results are stored.
```
iprscan = { 
    'results' : [ {
                 'sequence' = 'DQLNSEEKKKRKQRRNRTTFNSSQLQALERVFERTHY',
                   'matches' : [
                     {'accession': 'PTHR12027:SF93',
                      'evalue': 6.1e-88,
                      'goXRefs': [{'category': 'BIOLOGICAL_PROCESS',
                                   'databaseName': 'GO',
                                   'id': 'GO:0030182',
                                   'name': 'neuron differentiation'}],
                      'graftPoint': 'PTN000246818',
                      'model-ac': 'PTHR12027:SF93',
                      'name': 'PROTEIN WNT-2B',
                      'proteinClass': 'PC00207',
                      'score': 306.9
                     }
                    ]
                 },
         
                 { 'sequence' = 'GARVICDNIPGLVSRQRQLCQRYPDIMRSVGEGAR',
                   'matches' : [
                      {'evalue': 0.00034,
                       'model-ac': 'PF03826',
                       'score': 31.5,
                       'signature': {'accession': 'PF03826',
                                     'description': 'OAR motif',
                                     'name': 'OAR',
                         }
                       }
                    ]
                  }
             ]
          }
```

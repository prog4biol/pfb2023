Interproscan PTHR2GO
====================

We have a gene list we created for stem cell proliferation genes in alpaca in a [previous problemset](../../problemsets/Python_06_problemset.md). Let's look at these genes and see if there are any reoccurring GO terms or PFAM domains in our gene set.

Generate a FASTA file to use to predict protein domains and motifs using InterProScan. 


__Create FASTA for stem cell proliferation genes:__

1. Go to [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/3e66a7a80107043f1317566a8a10fed1).
2. In the "CHOOSE DATABASE" dropdown box, select "Ensembl Genes 110"  (or most current version)
3. In the "CHOOSE DATASET" dropdown box, select "Alpaca Genes" 
4. On the left, click Attributes
5. Expand GENE:
6. Deselect "transcript stable ID", "Gene stable ID version", and "transcript stable ID version".
7. These should be selected: Gene stable ID, Gene name, Gene description
8. Click "Filters"
9. Expand "GENE ONTOLOGY", then check "GO Term Name" and enter "stem cell proliferation" in the search box to its right (clear out any previous GO term names)
10. Click Attributes (left menu)
11. Then click the (o) for "Sequences" in the list of options near the top (Features, Homologues, Structures, Sequences)
12. Expand "SEQUENCES" and make sure the "Peptide" button is selected
13. Click Results (top left)
14. In the 'Export  all results to' field, input "File", then select "FASTA" from the dropdown menu, then click the GO button
15. On the command line, rename the saved "mart_export.txt" to "alpaca_stemcellproliferation_genes.fa"

__Predict Protein domains and motifs__

1. Go to the InterProScan Server: https://www.ebi.ac.uk/interpro/search/sequence
2. In the "by sequence" tab, paste in the contents of your stem cell proliferation FASTA file or choose the file for upload: "alpaca_stemcellproliferation_genes.fa"
3. Click the red "Automatic FASTA clean up" button. We have `*`s in our file for stop codons, InterProScan does not like those.
4. Click the teal "Search" button and wait until complete (~2 mins).
5. Once the search is complete, Click "Group Actions" (on the right), then select "Download All". You will get a JSON file that will be named similar to this: 20231021-172942-29.json
6. Parse the downloaded JSON file using the `json` module to "load" the data into your script. Extract the GO term information (`id` and `name`) from the PANTHER (`PTHR*`) matches data structure to see if there are recurring GO terms in our stem cell proliferation gene list. You can try this from scratch or use [my script](parseIPRSjson.py) and fill in a few keys to get the GO term information (`id` and `name`). 
7. See if there is a PFAM domain that is recurring in our stem cell proliferation gene list. Extract the PFAM (`PF*`) signature information (`accession`, `name`, and `description`) for each. You can try this from scratch or use my script and fill in a few keys to get the PFAM domain hits. 
8. If you finish all the other questions, look through your IPRSCAN results to pick another type of domain hit to add to your parser in a similar format to PFAM domains.



Here is an example of the JSON 2 Python data structure in which the PTHR and PFAM results are stored.
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
                                     'name': 'OAR'
                         }
                       }
                    ]
                  }
             ]
          }
```

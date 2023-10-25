GO Enrichment Hands On
======================
Instructions start on slide 64 of [lecture material](CSHL2023-function-and-enrichment.pdf)
- Download the files at      
  - http://data.pantherdb.org/ftp/tools/samples/
  - use [Piwi_2fold_down_id](http://data.pantherdb.org/ftp/tools/samples/Piwi_2fold_down_id) first
  - Do Enrichment analysis at [PANTHER DB](https://www.pantherdb.org/) with [Piwi_2fold_down_id](http://data.pantherdb.org/ftp/tools/samples/Piwi_2fold_down_id)
- They are from the publication  
  - https://www.ncbi.nlm.nih.gov/pubmed/26780607
 




Interproscan PTHR2GO Workshop
====================

We have a gene list we created for stem cell proliferation genes in alpaca (mentioned in a [previous problemset](../../problemsets/Python_06_problemset.md)). Let's annotate these genes and assess if there are any reoccurring GO terms or Pfam domains in this gene set. 

## Overview
- You will need to create a FASTA file of the protein sequences of a curated list of genes using Ensembl Biomart. (see steps below)
- Predict protein domains and motifs that are contained in our protein sequences using InterProScan. (see steps below)
- Review PANTHER protein family hits and extract associated Gene Ontology (GO) Term information for each of our proteins, PANTHER2GO. 
- Review InterPro hits and extract associated Gene Ontology (GO) Term information for each of our proteins, InterPro2GO. 
- Review Pfam protein domain hits and extract domain information for each of our proteins.
- Count up and compare the PANTHER2GO and InterPro2GO terms associated with your genes. 
- Review your GO terms and Pfam domains combined across all proteins to try to discern if there are any overlapping annotations in our curated gene list.
- Think about enrichment analysis.


### Generate a FASTA file of our stem cell proliferation gene set to use in prediction of protein domains and motifs using InterProScan. 


#### Create FASTA for stem cell proliferation genes:

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

Note: If you are having issues using Biomart to download the protein fasta, the file can be found in the same directory as this file (see below). The same is true for InterProScan Webserver JSON output for this protein protein FASTA. 


#### Predict Protein domains and motifs:
1. Go to the InterProScan Server: https://www.ebi.ac.uk/interpro/search/sequence
2. In the "by sequence" tab, paste in the contents of your stem cell proliferation FASTA file or choose the file for upload: "alpaca_stemcellproliferation_genes.fa"
3. Click the red "Automatic FASTA clean up" button. We have `*`s in our file for stop codons, InterProScan does not like those.
4. Click the teal "Search" button and wait until complete (~2 mins).
5. Once the search is complete, Click "Group Actions" (on the right), then select "Download All". You will get a JSON file that will be named similar to this: 20231021-172942-29.json

#### Parse the Protein prediction output
1. All of the subsequent tasks can be completed by creating your own script from scratch or by making edits to [the provided script](parseIPRSjson.py). The code has a few '?' where dictionary keys need to be inserted. The code will not run until this are filled in. This is the task #3: PATNER2GO and task #4: Pfam Domain. After this is completed, the code will run (as long as no other error were introduced). 
2. Parse the downloaded JSON file (produced by our InterProScan search) using the `json` module to "load" the data into your script.
  - First thing you should do is open your output file and look at it. MOST output files from MOST bioinformatic tools are flat text files. This means you can open them with any text editor like `vi`. You can also `head`, `less`, `more`, or `cat` them. This particular output file is large and has a lot of text and isn't super easy for human eyes to read. It is in JSON format which is a format that is used to make output parsable by scripts. There are a lot of key/value pairs in JSON, the keys are standarized and will be the same in every InterProScan JSON output.
3. PANTHER2GO
  -  Extract the PANTHER2GO term information. These are the GO terms associated with PANTHER hit records. You will need the `id` and `name` from the PANTHER (`PTHR*`) _matches_ data structure (see summary datastructure below).
  -  Save the terms in a dictionary to create a counter, `panther2go[goterminfo]=+1`, to see if there are recurring PANTHER2GO terms in our stem cell proliferation gene list.
  -  You can try this from scratch or use [the provided script](parseIPRSjson.py) and fill in a few keys to get the GO term information (`id` and `name`). 
4. Pfam Domains
  - In the same script from above, in a similar way, extract Pfam (`PF*`) hit information.
  - You will need the `accession`, `name`, and `description` from the Pfam (`PF*`) _signature_ data strucutre (see summary datastructure below).
  - Save the terms in a dictionary to create a counter, `pfam[pfinfo]=+1`, to determine if there is a Pfam domain that is recurring in our stem cell proliferation gene list.
  - You can try this from scratch or use [the provided script](parseIPRSjson.py) and fill in a few keys (`accession`, `name`, and `description`) to get the Pfam domain hits.
  -  The [the provided script](parseIPRSjson.py) should now have the '?' replaced with the appropriate keys and is now able to be run. Run it and review the output.

5.InterPro2GO
  - Extract the InterPro2GO term informatoin. These are GO terms associated with InterPro hit records.
  - To your script, add a block to get the GO term from InterProScan hit section. This is found in the _entry_ data structure (see summary datastructure below).
  - Use the Pfam python block and the PANTHER python blocks as a model.ccv

6. The format of the results that are printed to the screen in [the provided script](parseIPRSjson.py) are not pretty. Think about what is a useful way to look at this data
  - Reformat them in a tab delimeted format that can be opened in a spreadsheet.
  - Perphaps separating out the id, name, and description in the concatenated string would be nice.
  - Adding the GO category (Biological Process, Molecular Function, Cellular Component) could also be helpful. These can be retrieved from the datastructure in a similar way as the GO id and name.
    
7. Review your results.
  - What do you think?
  - Are the GO terms reasonable?
  - Do they make sense considering we have a list of predicted stem cell proliferation genes?
  - How do the PANTHER2GO and InterPro2GO term sets compare? Are the the same/different?
    
8. Think about GO enrichment. If you were going to do GO enrichment (we are not asking you to, but we won't stop you if you wanted to explore this topic) how would you do it?
  - Is one curated gene set enough? Do you need a background gene set to compare? If so, what would it be in our example?
  - What statistical test or tests would you perform?
  - Is there a python module to help with this?
        
9. Look through your IPRSCAN results (the JSON **file**) by opening it with a text editor to pick another type of domain/motif hit (i.e, Coils, TMHMM, SignalP_EUK). Add code to your parser, following a similar format to Pfam domain extraction, to extract the new protein domain/motif information to create a count and report your gene hits.


#### summary datastructure
Here is an example of the JSON 2 Python data structure in which the PTHR and Pfam results are stored.
```
iprscan = { 
    'results' : [ {
                 'sequence' = 'DQLNSEEKKKRKQRRNRTTFNSSQLQALERVFERTHY',
                   'matches' : [
                     {'accession_: 'PTHR12027:SF93',
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
                         },
                       'entry' : {
                         'accession' : 'IPR001356',
                         'name' : 'Homeobox_dom',
                         'description' : 'Homeobox domain',
                         'type' : 'DOMAIN',
                         'goXRefs' : [ {
                             'name' : 'DNA binding',
                             'databaseName' : 'GO',
                             'category' : 'MOLECULAR_FUNCTION',
                             'id' : 'GO:0003677'
                           } ],  
                       }
                     }
                   ]
                 }
             ]
          }
```

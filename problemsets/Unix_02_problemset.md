# Unix 2 Problem Set

1. Go to GitHub and create a free accout.

2. Look back at the notes and create your SSH key and add it to your github account.  [Notes for key creation](https://github.com/prog4biol/pfb2023/blob/master/unix.md#generating-a-new-ssh-key)
 
 #### Create Key and passphrase
```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```

```
> Enter a file in which to save the key (/Users/YOU/.ssh/id_ALGORITHM: [Press enter]
```

```
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

#### Adding your SSH key to the ssh-agent
```
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```

#### Add Key info to ssh configuration file
```
$ vi ~/.ssh/config
```
##### then add
```
Host *
  IdentityFile ~/.ssh/id_ed25519
```

#### Add to your GitHub.com account: Settings --> SSH and GPC Keys --> Click "New SSH Key"
Paste the contents of your public "Lock" to GitHub with a title
```
cat ~/.ssh/id_ed25519.pub
```

3. Create your first repository for your problem set code. [Notes for repository creation](https://github.com/prog4biol/pfb2023/blob/master/unix.md#git-for-beginners).
   **NOTE: Don't create a repository inside of another repostitory.**
   - Create a new Repository by clicking "New" on the repository github page. https://github.com/YOURUSERNAME/repositories 
   - Create a local (your machine) directory with `mkdir <dirname>` 
   - move into the new directory with `cd <dirname>` 
   - start setting up your repository with the code produced by github. Start with `git init`. 
   - **Don't `git init` in your home directory. Make a new directory (something like pfb_problemsets or problemsets or problem_sets), change directory into the new directory, then `git init`** 
   - Now link it to your remote repository with `git remote add`.

3. Move any files you created in Unix_01 Problem set to your local problemset git repository.

4. Push all the new files in your local repository to your remote repository
   - `git status` to see all the files you need to add
   - `git add <filename>`  or  `git add <filename1> <filename2> <filename3> ...`  
   - `git commit -m 'adding previous problem set files'`
   - `git push`
   - Visit the your GitHub repository website (on github.com) and see the files from your local repository that you just pushed up to your remote repository.



6. Create a directory call `files` in your ProblemSets directory. 

7. Move the file you renamed from `sequences.nt.fa` to `cancer_genes.fasta` to your `files` directory

8. ADD/COMMIT/PUSH `cancer_genes.fasta` to your remote repository
  - `git add files/cancer_genes.fasta`
  - `git commit -m 'adding cancer_genes.fasta'`
  - `git push`
  - Visit the your GitHub repository website (on github.com) and see the file from your local repository that you just pushed up to your remote repository.

9. Using your vi text editor create a fasta file and name it `mysequences.txt`. Make sure it ends up in your problem sets files directory.

This is fasta file format:
```
>seqName description
ATGGCGTCTTGGCCTTAAAAGCTC
GGCGTCTTGGCCTTAAAAGCTCAT
ATTCTTGGCCTTAAATTGGCCTTG
```
  - add 10 lines of sequence
  - delete a line
  - insert a new line at line 4
  - Copy line 5
  - Paste this line above line 2
  - set to view line numbers
  - Cut line 3 and paste below line 6
  - Go to line 4
  - delete a line
  - undo your last delete
  - search for `CTT`
  - find next occurance of `CTT`
  - Save and exit


10. ADD/COMMIT/PUSH `mysequences.txt` to your remote.


11. Create a directory called `fastas`.     (Hint: use mkdir)
12. Copy the fasta file that you renamed to `cancer_genes.fasta` to the fasta directory.
13. Verify that the file is within the fasta directory.  
14. Delete the the original file that you used for copying.  
15. Sync your remote repo with your local repo. Make sure to add each file you changed or use `git add <filename>`. Don't forget to commit and push.
16. Practice with `git rm`
  - Create a file named `oops` and add a few characters of content.
  - Save and Exit. 
  - Add/Commit/Push this file 
  - `git rm oops` 
  - `git commit -m 'removing oops'`
  - `git push`
17. Practice with `rm`. Can you spot the little difference from `git rm`
  - Create a file named `oops2`. add some content. save and exit
  - Add/Commit/Push this file
  - `rm oops2`
  - `git add oops2`
  - `git commit -m 'removing oops2'`
  - `git push`
18. Imagine this: You created a file, `git add` it, but then realize you don't want to commit it. What do you do? [from google search](https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit)
  - Create a file named `never`. 
  - `git add never`
  - `git reset never`
19. Read the man page for `rm` and `cp` to find out how to remove and copy a directory.
20. Print out your history and redirect it to a file called `unixBasics.history.txt`
21. Open your history file with your text editor and delete any lines you do not want to keep. See this [google search](https://www.google.com/search?rlz=1C5CHFA_enUS596US596&q=vi+delete+entire+line&oq=vi+delete+entire+line&gs_l=psy-ab.3..0j0i5i30k1.28765.29854.0.30351.7.6.0.0.0.0.186.526.0j3.3.0....0...1.1.64.psy-ab..5.2.362...0i13k1j0i7i5i30k1.0.Ub2zfH_lp_o) for info on deleting entire lines in vi.
22. Make sure all your files are synced with your remote repository. (`git status`)

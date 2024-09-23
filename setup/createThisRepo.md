# Create this Repo

To create this repo I duplicated last year's repo with these notes:  
https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository

1. Create a new empty repository on github.com for the new copy
2. Open Terminal.  
3. Create a bare clone of the repository.  
  `git clone --bare https://github.com/EXAMPLE-USER/OLD-REPOSITORY.git`  
4. Mirror-push to the new repository.  
   `cd OLD-REPOSITORY.git`  
    `git push --mirror https://github.com/EXAMPLE-USER/NEW-REPOSITORY.git`  
5. Remove the temporary local repository you created earlier.  
    `cd ..`  
    `rm -rf OLD-REPOSITORY.git`  

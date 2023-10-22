# Conda Package Manager

### Resources:
- [Conda Cheat Sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## What is Conda and why should you use it?

The [Conda](https://docs.conda.io/en/latest/) Python toolkit is a collection of tools for creating and managing virtual environments --- (semi-)self-contained Unix and/or Python command-line configurations --- that allow flexible installation of and access to the executables and libraries needed to perform different analyses. Conda can be used to install third-party software in addition to Python modules, and it tracks the specific version and build information for each install. This promotes reproducibility and transparency of data analyses, making Conda a valuable component of the scientific software stack.

There are two main distributions of Conda:

1.  [Miniconda](https://docs.conda.io/projects/miniconda/en/latest) : Contains the Conda command-line package manager, plus the Python interpreter with a minimal set of libraries/modules installed.

2.  [Anaconda](https://www.anaconda.com) : Contains the tools provided in Miniconda, but also includes a suite of various graphical tools useful for data science, machine learning, AI, among others.

## The basics

### How to create an environment:

The following will create a minimal (i.e., "empty") virtual environment called `envName`:

``` bash
$ conda create --name envName
```


### How to load/activate an environment:

To run executables or import libraries installed in a virtual environment, you first need to activate it. When you activate a Conda virtual environment, the new environment inherits your current Unix environment (so you'll still be able to use `ls`, etc., for example), but now gives you access to tools that are installed in `envName`:

``` bash
$ conda activate envName
```

### How to search for available software:

Conda can search for software of interest from the command line. The command below will search for the `pkgName` software package and write out the versions and builds available for installation.

``` bash
$ conda search pkgName
```

For example, to search for the `wget` Unix command-line tool:

``` bash
$ conda search wget
```

### How to install software:

You can install one or more software packages easily with Conda. It will first examine the software versions already installed in your loaded environment (if applicable), determine whether the package being installed has any unsatisfied dependencies, and create a list of dependencies (if any) that also need to be installed. This is what Conda calls "Solving your environment".

By default, Conda then installs the software package requested. If no package version was specified, Conda will choose a compatible version for you. If the software being installed was written in a compiled language --- such as C, C++, Java, etc. --- Conda will choose a pre-compiled build appropriate for your system. This saves you time and avoids many headaches caused by the often-tedious compilation process.

> NOTE: To install software into a virtual environment, you must first `conda activate` your environment or specify the `--name envName` option.

``` bash
# assuming that envName is activated
$ conda install pkgName1 pkgName2 ...

# or, when not activated, us the `--name` option:
$ conda install --name envName pkgName
```

If you want to specify a particular version (and build) of a tool you want to install, include the version, and optionally the build identifier, after the package name separated by equal (`=`) signs (the square brackets `[]` below denote optional components of the command):

``` bash
$ conda install pkgName[=Version[=Build]]
```

> NOTE: To install software into a virtual environment, you must first `conda activate` your environment or specify the `--name envName` option.

For example:

1.  Search for the software you want to install with Conda:

    ``` bash
    $ conda search wget
    Loading channels: done
    # Name                       Version           Build  Channel
    wget                          1.19.1      hcb5d8a9_0  pkgs/main
    wget                          1.19.4      h073198b_0  pkgs/main
    wget                          1.19.5      h051b688_0  pkgs/main
    wget                          1.19.5      hf30b1f0_0  pkgs/main
    wget                          1.20.1      h051b688_0  pkgs/main
    wget                          1.20.1      h33e2efd_0  conda-forge
    wget                          1.20.1      hb1dc21d_0  conda-forge
    wget                          1.20.3      h52ee1ee_0  conda-forge
    wget                          1.20.3      h52ee1ee_1  conda-forge
    wget                          1.20.3      hd3787cc_1  conda-forge
    wget                          1.21.3      h6dfd666_0  pkgs/main
    wget                          1.21.4      ha585b31_1  pkgs/main
    wget                          1.21.4      he369b6f_0  pkgs/main\
    wget                          1.21.4      hf20ceda_1  pkgs/main
    ```

2.  Then choose the version (and build) you want to install:

    ``` bash
    $ conda install wget=1.19.1=hcb5d8a9_0
    ```

### How to check packages already installed:

Conda provides an utility to interrogate which packages (and their versions and builds) are installed in your environment. This can be useful when writing up your Methods sections!

``` bash
# Assuming your environment is activated
$ conda list

# If the `envName` environment was not already activated
$ conda list --name envName
```

For example:

``` bash
$ conda list
# packages in environment at /Users/jbredeson/miniconda3:
#
# Name                    Version                   Build  Channel
brotlipy                  0.7.0           py39h9ed2024_1003  
bzip2                     1.0.8                h1de35cc_0  
c-ares                    1.19.1               h6c40b1e_0  
ca-certificates           2023.08.22           hecd8cb5_0  
certifi                   2023.7.22        py39hecd8cb5_0  
cffi                      1.15.1           py39h6c40b1e_3  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
conda                     23.1.0           py39hecd8cb5_0  
conda-package-handling    2.2.0            py39hecd8cb5_0  
conda-package-streaming   0.9.0            py39hecd8cb5_0  
cryptography              41.0.3           py39h30e54ef_0  
fmt                       9.1.0                ha357a0b_0
```

### How to update/upgrade Conda packages:

One can also update older software versions:

``` bash
$ conda update pkgName1 pkgName2 ...
```

To update a single package:

``` bash
$ conda update wget
```

Update *all* packages in your environment:

``` bash
$ conda update --all
```

To update a package to a specific version, use `conda install` instead:

``` bash
$ conda install wget=1.21.4=hf20ceda_1
```

### Remove packages from an environment:

``` bash
$ conda remove pkgName1 pkgName2 ...
```

> NOTE: To remove software from a virtual environment, you must first `conda activate` your environment or specify the `--name envName` option.

### Which Conda virtual environments do I have?

It's convenient to organize tools into environments by analysis type (i.e., one for genome assembly tools, another for variant calling tools, and another for RNA-seq analysis, etc.). This, however, can result in many Conda environments. We can see which environments we have by running

``` bash
$ conda env list
```

## Other useful commands

### Adding channels

There are many sources of software packages that you can install from, which are stored on servers on the web. In Conda parlance, these source servers are referred to as "channels". Some useful bioinformatics channels can be added to your Conda configuration like so:

``` bash
$ conda config --add channels bioconda
$ conda config --add channels anaconda
$ conda config --add channels conda-forge
```

> NOTE: With each of the above `conda` commands, you can specify particular channels without adding them to your Conda configuration permanently by including the `--channel channelName` option. This option can be specified more than once on the command line.

### Reproducible environments

Conda provides a convenient utility allowing you to export the list of software (and their version and build information) installed in an environment, allowing you to share that environment with others via a compact text file. This is useful when writing your Methods sections, allowing reviewers to run your analyses themselves, increasing reproducibility.

The command below will write a [YAML](https://yaml.org)-formatted file called `envName.yaml` containing the information required to reproduce an environment.

``` bash
$ conda env export --file envName.yaml
```

One can then re-create that environment from the YAML file:

``` bash
$ conda env create --file envName.yaml --name envName
```

### Testing a single executable command

Sometimes, for testing purposes, it may be necessary to run a single executable installed in the environment without activating the environment. One can do this by using the `run` command:

``` bash
$ conda run --name envName softwareCommand
```

For example:

``` bash
$ conda run --name bioEnv samtools depth my.bam >my.depth
```

### Remove cached temporary files

When Conda installs software in environments, it downloads and caches TAR archive files containing the software (for each version) installed. After a while, these TAR files can accumulate and occupy many gigabytes of disk space. You can remove these cached TAR files with the `clean` command:

``` bash
$ conda clean --all

Will remove 464 (805.8 MB) tarball(s).
Proceed ([y]/n)? y

Will remove 1 index cache(s).
Proceed ([y]/n)? y

Will remove 96 (324.7 MB) package(s).
Proceed ([y]/n)? y

There are no tempfile(s) to remove.
There are no logfile(s) to remove.
```

# Developer Guide

Thank you for joining us to work on this project! We hope that here you will find useful information to help you get started. If you think of anything that should be added, feel free to raise an issue and propose the change.

## Setting up virtual environment
To avoid confusion about which versions of python and any packages are being used, it's a good idea to work in a *virtual environment*.
Here's how to set one up:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r contributor_requirements.txt
```
#TODO: make contributor_requirements.txt file

## Workflow 
Pick an issue to work on and assign yourself to that issue. 
Check out a new branch by typing in the console
```bash
git checkout -b <branch name>
```
Replace the contents of <> with your chosen branch name. It should include the number of the issue you've chosen to work on, as well as a short description of the issue in a few words. 

After making your improvements, run `git diff` in the console to satisfy yourself that you haven't changed anything other than what you intended to. Add and commit any changed files with an informative commit message beginning with a reference to the issue number:
```bash
git add <filename1> <filename2> <...>
git commit -m "#<issue number> <description of changes>"
```
Then you can push those changes to your branch:
```bash
git push origin <branch name>
```
The console will print out a link which you can follow to create a pull request. Another contributor will then review your changes and merge them into the master branch, or ask you to make some more changes before merging. 

## Naming conventions

Most methods and functions have one-word names. Where the name consists of multiple words, these are connected by an underscore (_). 
Variable names are kept consistent with the model equations that form the base of [this library's functionalities](https://github.com/smf541/PK-Group5#pk-model, "Functionality")). 

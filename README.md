# ECE_4983-4984_Path_Following_Delivery_Robot

## Cloning this Repository

### In Github Desktop 
1. Install Github Desktop
2. Login with your Github account
3. In this repository, go to '<>Code' dropdown
4. Select 'Open with Github Desktop'
5. Save this repository to a location outside of iCloud Drive/OneDrive

### With GIT
1. Set up SSH Key inside of Github Settings
2. Clone Repository through Terminal using SSH Key under '<>Code' dropdown

**Specific Instructions:** https://docs.github.com/en/authentication/connecting-to-github-with-ssh

## Making Sure You're on Your Own Branch

### In Github Deskop
1. Ensure your name is included under 'Current Branch' dropdown

### With GIT
1. In Terminal, open at the file in which you saved this repository
2. For Windows, Right Click on file location for repository, select 'Git Bash Here' (likely under More Options)
3. 'git checkout 'name of your branch'
**EX:**
    - git checkout Gina
    - git checkout Yehya

## Updating your Branch with Current Code

### In Github Desktop 
1. Fetch Origin

### With GIT
1. In Terminal, open at the file in which you saved this repository
2. 'git pull origin main' 

## Before Setting a Push Request (!!!)
* Demonstrate to the group that your code works on the Raspberry Pi
    - Can checkout your Branch on RPi to demonstrate
* Update ChangeLog.md with all additions and accomplishments
    - Include important notes if any
* Ensure all changes are included 
    - Additions show green [+]
    - Deletions show red [-]
    - Save all updated files if changes not updated 
* Ensure all files you've changed or added are included in push request
    - 'git add Name_of_File.py'
    - In Github Desktop, all files changed will show up on the lefthand side

## To Push to Main 
* (!!!) All push requests have to be approved before they can be reflected in Main program

### In Github Desktop 
1. Add Summary Describing your Changes
2. Add Useful/Descriptive Caption to Commit
3. Click "Commit to 'branch'" Button
4. Click 'Pull Origin' button
5. Click 'Preview Pull Request' button
6. Create pull request 

**PULL = PUSH in this case**

### With GIT
1. In Terminal, open at the file in which you saved this repository
2. 'git -am "Include a Caption"'
3. 'git push' 


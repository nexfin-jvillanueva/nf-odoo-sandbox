# ⚠️ Welcome to NexFin's Odoo Sandbox! ⚠️

The purpose of this repository is to provide NexFin the ability to develop custom applications in Odoo via GitHub.

## Creation of Custom Module
Odoo.sh > create development branch

To clone the GitHub repository:
$ mkdir ~/src        # Create a directory to store your projects (if it doesn't exist)
$ cd ~/src           # Navigate to the 'src' directory
$ git clone git@github.com:nexfin-jvillanueva/nf-odoo-sandbox.git  # Clone your repo
$ cd nf-odoo-sandbox  # Move into the cloned directory

❗ Error: 
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

⚠️ Resolution: Generate SSH Key and add to SSH Agent
ssh-keygen -t ed25519 -C "jvillanueva@nexfinitsolutions.com"

Run the following command to display your SSH public key:
$ cat ~/.ssh/id_ed25519.pub

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPCmcWG3SD3QPNynmxKZngZuaR+Kb5oUw08UfEFj6zEi jvillanueva@nexfinitsolutions.com
Add to GitHub!

Then try cloning again

Make directory for the custom module:
$ mkdir RE-module

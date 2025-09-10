# WEEK 1

The task today is to get setup with git/github and make changes to your own branch.

The first goal is to make an edit to a file so everyone can see it in the remote repository.

Before you do anything, you need to create and switch to your own branch. You can do this by typing:
`git branch <your name>` to create your own branch, then
`git checkout <your name>` to switch to your own branch.

First, with any text editor of your choice, edit the file in this directory called editme to say a message of your choice

Once you've saved this file with your changes, you need to _stage_ the change. git doesn't care about a file until you tell it to.

To stage a change, type the command `git add editme`
Now, commit the change with a command like `git commit -m "added message to editme"`
Finally, to move your commit from your computer to the Github repo use the command `git push --set-upstream origin <your name>`
The reason you needed to use the --set-upstream flag is because you just created this branch on your computer but Github was never aware of it until you ran that command.
All future pushes on this branch will just require you to run `git push`

Let me know when you get that done so I can see if I can view your message from my computer.

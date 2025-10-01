# WEEK 2

Today we are going to use our python experience to do some basic networking

We are going to begin by sending messages between processes on your own computer, which in practice is no different than sending them between computers

The way we send messages over the internet is with TCP or UDP. TCP guarantees that data is sent and is in order, while UDP just sends everything and hopes it makes it to where it needs to go. For more information on the differences between the two, you can read this website: https://www.geeksforgeeks.org/computer-networks/differences-between-tcp-and-udp/

## Using TCP

There is some code in the /tcp/ folder to get you started sending tcp messages between processes on your own computer.

There are only a few things you need to fill in here to get you going:
- The HOST in the sender and receiver. You must look up what this ip address is for your personal device.
- The port number. You must choose this number based on the comments in the code. It must match between the sender and receiver files. (Call me over and explain why)
- The message that you want to send in the receiver. You can send whatever you want as long as theyre just normal characters.

A couple questions (Call me over and answer them):
Which file should you run first and why?
Why does the receiver have a loop and the sender doesn't?
Why can you choose the port number but not the IP address?
What does AF_INET mean and what does SOCK_STREAM mean? (look it up)

Now that you have answered all these questions, group up with someone else who has also answered them. Your task now is to send messages over a network to each others computers instead of to your own computer (Tell me when you are going to start this).
A couple questions to get you in the right direction:
- Should the port number be the same or different between computers?
- What is the IP address to listen for messages from _all_ other devices? (look it up)

## Using UDP

If there is still time, do the same tasks as above but using UDP. The task is very similar, but requires some slight changes to the tcp code. 
_Hint:_ What is the thing that says to use TCP in the TCP code?

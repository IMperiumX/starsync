# starsync

Power of async await with the simplicity of python code.

## TL:DR

async programming capabilities for python whereis to performe multi task concurrently

## IDEA of Async programming

provide a way to run multiple long running task side by site independently of each other.

## Key Cirteria of Async programming

**key ciretrian** for such tasks involve **wating** for something else **not** performing something **cpu intensive**:

e.g: reading from multiple network connections at once because you **spent vast amount of your time wating to read** from a network instead of reading data or working with it.

use the waiting time **efficently** by **switing** between each read operation to see if it finished yet istead of reading from one internet connection wating it to finishes, moving on the next one wait that to finish and so on and forth

is this example i want to un-start mine repositories with github api

taking that action of listing all availabe repos storing them into file

calling github api again with detele request to unstart it given username/repo

with sync method it took in average of 30sec

![](assets/images/WhatsApp%20Image%202022-10-26%20at%204.52.18%20PM.jpeg)

but with async method  it only took in average about 3sec.

which is 10X faster
![](assets/images/Screenshot%202022-10-26%20165043.jpg)

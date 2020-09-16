# ROS Basics
This repository consists of a small hello world program and rrbot controller.


## Hello World for ROS

Most of us started our coding with a hello world program. We can do the same with ROS.
We need a publisher node, a subscriber node and a topic to know how ROS communicates.
I made a package named "hello_world". It consists of a folder called scripts. We can add all out python scripts here in this folder. It is not mandatory but it is a good practice to arrage them in a separate folder.
We have two files 'talker.py' and 'listener.py'. The talker.py consists of a node called talker which publishes a String, let's say 'U there?', to the topicc called 'Chat'. The listener.py conssist of a node called listener which subscribes the topic 'chat' and confirms with a text 'Yupp'.

### How to Run?

We can run the scripts using the command "rosrun package_name file_name".

### Here's how it works
![](img/hello_world.png)

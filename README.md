This algorithm aims to attach artificial intelligence to a robot that is capable of interacting with its environment. This would add capabilities such as navigating adverse environments (such as yards) using Visual Simultaneous Location and Mapping (VSLAM) technologies and Image recognition models. To further improve decision-making and allow for more complex commands and interactions with the environment an LLM would be used as an embodied artificial intelligence agent. 

Installation and Requirements: 
 Leaf Vac requires a machine that contains a camera, a processor(for transmitting data and motion control), two motors for navigating the environment, and a claw to interact with objects. The cameras should then be calibrated using the calibration.py within the src folder. Once the initial setup is complete the robot will then ask for a request from the user, some tested requests are "find my *item*" or "drive x feet *direction*". Future features will include the option to map out its current environment by roaming within an allocated area and creating a 3D map of that area that includes all obstacles while differentiating permanent obstacles(such as trees or houses) and non-permanent obstacles(such as pets).


This will be using an image recognition model to identify obstacles in the area allowing the robot to take different actions in response to every different obstacle(ignore animals, navigate around trees, pick up sticks and leaves, etc…).


Additionally, it should also be able to export the three-dimensional map created onto some algorithm to allow users to specify non-approachable areas (areas the robot isn't allowed to go into like flower beds), or plan to decorate their yard (add trees in specific locations within the 3d map to visualize how that will look). 


This algorithm could be used in many industries such as landscaping to visualize and plan the yard, or to assist people clean their yard from leaves and other debris. It could also be equipped onto a lawn mower to direct it to avoid specific areas or specific plans and have specific designs for the grass.


Throughout the first few weeks, I will conduct research on the specifications required on the cameras and the calibration process for depth recognition on stereo cameras systems. I will also research the best image identification Reinforcement Learning models that are optimal for outdoor usage.


Semester Goals:


By the end of September, we should have completed a 3D-printed claw and have it attached to the robot being controlled remotely from the a PC

By the end of September,  we plan to have mounted cameras on the robot to be used for testing and fine tuning the Reinforcement Learning models for Image detection.

 By the end of October, we should have created an algorithm that processes the images from the camera and creates a 3D model of the area. 

By November we should have multiple image recognition models selected and benchmarked to select one that is resource efficient given the limited processing power that could be attached to a small robot while being accurate enough to detect the different objects usually found on lawns.

David Rowe : rowed4
By the beginning of October, we should have selected and prepared the preferred hardware to work on for the robot
By the end of of october, we should have a power schematic for the robot and possibly some of the circuity completed.
By the Middle of november, we should have code written for the preffered hardware like arduino so that we can communicate wirelessly with bluetooth to the robot.
By Decemeber, we should be able to test a functional robot that can complete basic tasks wirelessly

Ruoxiang Zhao 662036700
Task:
3D model main body by 10/20
Build functional motion system by 10/25
Test mech system
Model and 3D print a robotic arm for the robot by 11/20

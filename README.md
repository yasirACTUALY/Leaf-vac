This algorithm aims to attach artifical intelligence into a robot that is capable to interact with its enviroment. This would add capabilities such as navigating adverse enviroments(such as yards) using Visual Simultaneous Location and Mapping (VSLAM) technologies and Image recognition models. T further improve decision making and allow for more complex commands and interactions with the enviroment an LLM would be used as an embodied artifical intellegnce agent. 

Installation and Requirements: 
 Leaf Vac requires a machine that contains camera, a processor(for transmiting data and motion control), two motors for navigating the enviroment, and a claw to interact with objects. The cameras should then be calibrated using the calibration.py within the src folder. Once the initial set up is complete the robot will then ask for a request from the user, some tested request are "find my *item*" or "drive x feet *direction*". Future features will include the option to map out its current envirment by roaming within an allocated area and creating a 3D map of that area that includes all obstacles while differentiating permanent obstacles(such as trees or houses) and non-permanent obstacles(such as pets).


This will be using an image recognition model to identify obstacles in the area allowing the robot to take different actions in response to every different obstacle(ignore animals, navigate around trees, pick up sticks and leaves, etc…).


Additionally, it should also be able to export the three dimensional map created onto some algorithm to allow users to specify non-approcable area(areas the robot isn't allowed to go into like flower beds), or plan to decorate their yard (add trees in specific locations within the 3d map to visualize how that will look). 


This algorithm could be used in many industries such as landscaping to visualize and plan the yard, or to assist people clean their yard from leaves and other debris. It could also be equipped onto a lawn mower to direct it to avoid specific areas or specific plans and have specific designs for the grass.


Throughout the first few weeks, I will conduct research on the specifications required on the cameras and the calibration process for depth recognition on stereo cameras systems. I will also research the best image identification Reinforcement Learning models that are optimal for outdoor usage.


Semester Goals:


By late June we plan to have mounted cameras on the robot so that it could be used for both testing and fine tuning the Reinforcement Learning models for Image detection.


 By the end of July we should have created an algorithm that processes the images from the cameras and passes the data through RL models to and starts fine tuning the models for specifically yard navigation. 


By early July we should have multiple image recognition models selected and benchmarked to select one that is resource efficient given the limited processing power that could be attached to a small robot while being accurate enough to detect the different objects usually found on lawns.

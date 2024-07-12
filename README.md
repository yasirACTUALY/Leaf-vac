OverLeaf is aimed to be an algorithm that would allow smart robots to navigate yards using Visual Simultaneous Location and Mapping (VSLAM) technologies and Image recognition models. Leaf Vac should be easily installable on any machine that contains cameras, a processor, and the ability to move around its environment. The cameras should then be calibrated automatically or with minimal user input. Once the initial set up is complete the robot should be able to start roaming within its allocated area and creating a 3D map of that area that includes all obstacles while differentiating permanent obstacles(such as trees or houses) and non-permanent obstacles(such as animals and sticks.


This will be using a vision model to identify obstacles in the area  allowing the robot to take different actions in response to every different obstacle(ignore animals, navigate around trees, pick up sticks and leaves, etc…).


Additionally, it should also be able to export the three dimensional map created onto some algorithm to allow users to specify non-approcable area(areas the robot isn't allowed to go into like flower beds), or plan to decorate their yard (add trees in specific locations within the 3d map to visualize how that will look). 


This algorithm could be used in many industries such as landscaping to visualize and plan the yard, or to assist people clean their yard from leaves and other debris. It could also be equipped onto a lawn mower to direct it to avoid specific areas or specific plans and have specific designs for the grass.


Throughout the first few weeks, I will conduct research on the specifications required on the cameras and the calibration process for depth recognition on stereo cameras systems. I will also research the best image identification Reinforcement Learning models that are optimal for outdoor usage.


Semester Goals:


By late June we plan to have mounted cameras on the robot so that it could be used for both testing and fine tuning the Reinforcement Learning models for Image detection.


 By the end of July we should have created an algorithm that processes the images from the cameras and passes the data through RL models to and starts fine tuning the models for specifically yard navigation. 


By early July we should have multiple image recognition models selected and benchmarked to select one that is resource efficient given the limited processing power that could be attached to a small robot while being accurate enough to detect the different objects usually found on lawns.

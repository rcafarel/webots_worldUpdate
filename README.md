Inputs to this update script come from the simulated annealing algorithm and are added to the Inputs.py file.
The output of this script is a new world file which is written to Outputs.txt.
Currently there is only one injury type that can be modified from the inputs, frontRightS3_twistRadians. 
Other injuries can be added, just need to determine how the injury needs to be represented in the world file and add the variable to the WorldFileContent.py script.
  example: rotation 0 1 0 ''' + str(frontRightS3_twistRadians) + '''

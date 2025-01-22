
from WorldFileContent import preamble, uninjuredRobot, injuredRobot_preInjuredLeg, injuredRobot_injuredLeg, injuredRobot_postInjuredLeg

worldFileContent = preamble + uninjuredRobot + injuredRobot_preInjuredLeg + injuredRobot_injuredLeg + injuredRobot_postInjuredLeg

with open("../data/Output.txt", "w") as text_file:
    text_file.write(worldFileContent)

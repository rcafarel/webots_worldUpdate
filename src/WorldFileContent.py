import math
from data.Inputs import dh1_theta, dh1_d, dh1_a, dh1_alpha
from data.Inputs import dh2_theta, dh2_d, dh2_a, dh2_alpha
from data.Inputs import dh3_theta, dh3_d, dh3_a, dh3_alpha
from data.Inputs import dh4_theta, dh4_d, dh4_a, dh4_alpha
from data.Inputs import frontRightS3_twistRadians


injuredRobot_preInjuredLeg = '''
DEF robotDH Robot {
  translation -1 0 0.1
  children ['''


dh1_legLength = math.sqrt(dh1_d * dh1_d + dh1_a * dh1_a)
dh1_legAngle = math.pi + math.atan2(dh1_a, dh1_d)

dh2_legLength = math.sqrt(dh2_d * dh2_d + dh2_a * dh2_a)
dh2_legAngle = math.pi + math.atan2(dh2_a, dh2_d)

dh3_legLength = math.sqrt(dh3_d * dh3_d + dh3_a * dh3_a)
dh3_legAngle = math.pi + math.atan2(dh3_a, dh3_d)

dh4_legLength = math.sqrt(dh4_d * dh4_d + dh4_a * dh4_a)
dh4_legAngle = math.pi + math.atan2(dh4_a, dh4_d)


injuredRobot_injuredLeg = '''
    DEF frontRightDH Solid {
      translation 0.039 0.1 0
      rotation 0 0 1 0.785398
      children [
        DEF dhConnect Shape {
          appearance GlossyPaint {
            baseColor 1 0 0
          }
          geometry Box {
            size 0.01 0.01 0.01
          }
          castShadows FALSE
        }
        DEF dh1_Theta Solid {
          rotation 0 0 1 ''' + str(dh1_theta) + '''
          children [
            DEF dh1_DAAlpha Solid {
              translation ''' + str(dh1_a) + " 0 " + str(dh1_d) + '''
              rotation 1 0 0 ''' + str(dh1_alpha) + '''
              children [
                DEF dh1_servo HingeJoint {
                  jointParameters HingeJointParameters {
                    position 0
                    axis 0 0 1
                  }
                  device [
                    RotationalMotor {
                      name "dh_servo1"
                    }
                  ]
                  endPoint DEF dh1_sevoEndpoint Solid {
                    rotation 0 0 1 0
                    children [
                      DEF dh2_Theta Solid {
                        rotation 0 0 1 ''' + str(dh2_theta) + '''
                        children [
                          DEF dh2_servo1Shape Shape {
                            appearance ReflectiveSurface {
                            }
                            geometry Cylinder {
                              height 0.01
                              radius 0.005
                            }
                            castShadows FALSE
                          }
                          DEF dh2_DAAlpha Solid {
                            translation ''' + str(dh2_a) + " 0 " + str(dh2_d) + '''
                            rotation 1 0 0 ''' + str(dh2_alpha) + '''
                            children [
                              DEF dh2_servoShape Shape {
                                appearance ReflectiveSurface {
                                }
                                geometry Cylinder {
                                  height 0.01
                                  radius 0.005
                                }
                                castShadows FALSE
                              }
                              DEF dh2_servo HingeJoint {
                                jointParameters HingeJointParameters {
                                  position 0
                                  axis 0 0 1
                                }
                                device [
                                  RotationalMotor {
                                    name "dh_servo2"
                                  }
                                ]
                                endPoint DEF dh2_servoEndpoint Solid {
                                  rotation 0 0 1 0
                                  children [
                                    DEF dh3_servo2Shape Shape {
                                      appearance ReflectiveSurface {
                                      }
                                      geometry Cylinder {
                                        height 0.01
                                        radius 0.005
                                      }
                                      castShadows FALSE
                                    }
                                    DEF dh3_Theta Solid {
                                      rotation 0 0 1 ''' + str(dh3_theta) + '''
                                      children [
                                        DEF dh3_legSegment Solid {
                                          translation ''' + str(dh3_a / 2.0) + " 0 " + str(dh3_d / 2.0) + '''
                                          rotation 0 1 0 ''' + str(dh3_legAngle) + '''
                                          children [
                                            DEF dh3_legSegment_shape Shape {
                                              geometry Cylinder {
                                                height ''' + str(dh3_legLength) + '''
                                                radius 0.001
                                              }
                                            }
                                          ]
                                          name "solid(1)"
                                          boundingObject USE dh3_legSegment_shape
                                          physics Physics {
                                          }
                                        }
                                        DEF dh3_servo2Shape Shape {
                                          appearance ReflectiveSurface {
                                          }
                                          geometry Cylinder {
                                            height 0.01
                                            radius 0.005
                                          }
                                          castShadows FALSE
                                        }
                                        DEF dh3_DAAlpha Solid {
                                          translation ''' + str(dh3_a) + " 0 " + str(dh3_d) + '''
                                          rotation 1 0 0 ''' + str(dh3_alpha) + '''
                                          children [
                                            DEF dh3_servoShape Shape {
                                              appearance ReflectiveSurface {
                                              }
                                              geometry Cylinder {
                                                height 0.01
                                                radius 0.005
                                              }
                                              castShadows FALSE
                                            }
                                            DEF dh3_servo HingeJoint {
                                              jointParameters HingeJointParameters {
                                                position 0
                                                axis 0 0 1
                                              }
                                              device [
                                                RotationalMotor {
                                                  name "dh_servo3"
                                                }
                                              ]
                                              endPoint Solid {
                                                rotation 0 0 1 0
                                                children [
                                                  DEF dh4_servo3Shape Shape {
                                                    appearance ReflectiveSurface {
                                                    }
                                                    geometry Cylinder {
                                                      height 0.01
                                                      radius 0.005
                                                    }
                                                    castShadows FALSE
                                                  }
                                                  DEF dh4_Theta Solid {
                                                    rotation 0 0 1 ''' + str(dh4_theta) + '''
                                                    children [
                                                      DEF dh4_legSegment Solid {
                                                        translation ''' + str(dh4_a / 2.0) + " 0 " + str(dh4_d / 2.0) + '''
                                                        rotation 0 1 0 ''' + str(dh4_legAngle) + '''
                                                        children [
                                                          DEF dh4_legSegment_shape Shape {
                                                            geometry Cylinder {
                                                              height ''' + str(dh4_legLength) + '''
                                                              radius 0.001
                                                            }
                                                          }
                                                        ]
                                                        name "solid(1)"
                                                        boundingObject USE dh4_legSegment_shape
                                                        physics Physics {
                                                        }
                                                      }
                                                      DEF dh4_servo3Shape Shape {
                                                        appearance ReflectiveSurface {
                                                        }
                                                        geometry Cylinder {
                                                          height 0.01
                                                          radius 0.005
                                                        }
                                                        castShadows FALSE
                                                      }
                                                      DEF dh4_DAAlpha Solid {
                                                        translation ''' + str(dh4_a) + " 0 " + str(dh4_d) + '''
                                                        children [
                                                          DEF endEffector Shape {
                                                            appearance DamascusSteel {
                                                            }
                                                            geometry Sphere {
                                                              radius 0.005
                                                            }
                                                            castShadows FALSE
                                                          }
                                                        ]
                                                        boundingObject USE endEffector
                                                        physics Physics {
                                                        }
                                                      }
                                                    ]
                                                    boundingObject USE dh4_servo3Shape
                                                    physics Physics {
                                                    }
                                                  }
                                                ]
                                                boundingObject USE dh4_servo3Shape
                                                physics Physics {
                                                }
                                              }
                                            }
                                          ]
                                          boundingObject USE dh3_servoShape
                                          physics Physics {
                                          }
                                        }
                                      ]
                                      boundingObject USE dh4_servo3Shape
                                      physics Physics {
                                      }
                                    }
                                  ]
                                  boundingObject USE dh4_servo3Shape
                                  physics Physics {
                                  }
                                }
                              }
                            ]
                            name "solid(1)"
                            boundingObject USE dh3_servoShape
                            physics Physics {
                            }
                          }
                          DEF dh2_legSegment Solid {
                            translation ''' + str(dh2_a / 2.0) + " 0 " + str(dh2_d / 2.0) + '''
                            rotation 0 1 0 ''' + str(dh2_legAngle) + '''
                            children [
                              DEF dh2_legSegment_shape Shape {
                                geometry Cylinder {
                                  height ''' + str(dh2_legLength) + '''
                                  radius 0.001
                                }
                              }
                            ]
                            boundingObject USE dh2_legSegment_shape
                            physics Physics {
                            }
                          }
                        ]
                        boundingObject USE dh4_servo3Shape
                        physics Physics {
                        }
                      }
                      DEF dh2_servo1Shape Shape {
                        appearance ReflectiveSurface {
                        }
                        geometry Cylinder {
                          height 0.01
                          radius 0.005
                        }
                        castShadows FALSE
                      }
                    ]
                    boundingObject USE dh2_servo1Shape
                    physics Physics {
                    }
                  }
                }
                DEF dh1_servoShape Shape {
                  appearance ReflectiveSurface {
                  }
                  geometry Cylinder {
                    height 0.01
                    radius 0.005
                  }
                  castShadows FALSE
                }
              ]
              name "solid(1)"
              boundingObject USE dh1_servoShape
              physics Physics {
              }
            }
            DEF dh1_legSegment Solid {
              translation ''' + str(dh1_a / 2.0) + " 0 " + str(dh1_d / 2.0) + '''
              rotation 0 1 0 ''' + str(dh1_legAngle) + '''
              children [
                DEF dh1_legSegment_shape Shape {
                  geometry Cylinder {
                    height ''' + str(dh1_legLength) + '''
                    radius 0.001
                  }
                }
              ]
              boundingObject USE dh1_legSegment_shape
              physics Physics {
              }
            }
          ]
          boundingObject USE dhConnect
          physics Physics {
          }
        }
      ]
      name "solid(7)"
      boundingObject USE dhConnect
      physics Physics {
      }
    }'''

injuredRobot_postInjuredLeg = '''
    DEF middleRightLeg Solid {
      translation 0.092 0 0
      rotation 0 0 -1 1.5708
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.1529421931294168
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo13Motor"
            }
          ]
          endPoint Solid {
            translation 1.4720625941739795e-05 2.2117840916729457e-05 4.1781194690948525e-06
            rotation 6.901674450715985e-06 -7.288857453582907e-07 -0.9999999999759179 0.15294219323154842
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 -1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position 0.5025722540841397
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo14Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 -1 0.5025722540841399
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position 0.8535074290714773
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo15Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation 0 0 1 0.853507429071477
                                children [
                                  DEF ee_middleRightLeg Solid {
                                    translation -0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation -0.0505 0.0455 0
                                    rotation 0 0 -1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(3)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF backRightLeg Solid {
      translation 0.0585 -0.1195 0
      rotation 0 0 -1 2.35619449
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position 0.5405186274421339
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo10Motor"
            }
          ]
          endPoint Solid {
            translation 9.01044520139725e-06 7.563837330210504e-05 9.003554777564646e-07
            rotation -7.490414182856013e-05 -9.904669836886853e-05 0.9999999922895604 0.5405103114646254
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 -1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position 0.5678653500981593
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo11Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 -1 0.5678653500981591
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position 1.012809596143684
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo12Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation 0 0 1 1.0128095961436843
                                children [
                                  DEF ee_backRightLeg Solid {
                                    translation -0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation -0.0505 0.0455 0
                                    rotation 0 0 -1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(4)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF frontLeftLeg Solid {
      translation -0.0585 0.1195 0
      rotation 0 0 1 0.7853980000000005
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position 0.5328773876814623
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo7Motor"
            }
          ]
          endPoint Solid {
            translation 1.4905001457335633e-05 5.973774658797368e-05 3.0576497142553727e-07
            rotation 1.4159215778829767e-06 1.6068892515689373e-07 0.9999999999989846 0.5328773877320421
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.5677889554392861
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo8Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 1 0.5677889554392864
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -1.0127670268867315
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo9Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.09312243643560558 -0.008142311185534132 -0.9956213711049269 1.016493894430688
                                children [
                                  DEF ee_frontLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(1)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF middleLeftLeg Solid {
      translation -0.092 0 0
      rotation 0 0 1 1.570796327
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.15988997035738572
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo4Motor"
            }
          ]
          endPoint Solid {
            translation 1.2580739441467665e-05 1.893439143870153e-05 -1.2476656639781585e-06
            rotation 1.5929119570441178e-06 6.499607414754528e-08 -0.9999999999987291 0.15988997044072173
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.5025158088984756
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo5Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 0.9999999999999999 0.5025158088984758
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -0.8534669698537553
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo6Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.10784240482769301 -0.018164005235651204 -0.9940020546431377 0.8580093756079213
                                children [
                                  DEF ee_middleLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(5)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF backLeftLeg Solid {
      translation -0.0585 -0.1195 0
      rotation 0 0 1 2.35619449
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.24285843276271205
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo1Motor"
            }
          ]
          endPoint Solid {
            translation -3.163225929604362e-05 3.290629607933502e-05 2.342962135054582e-06
            rotation 2.8737723694855654e-06 1.3880800649851915e-07 -0.9999999999958611 0.24285843272054292
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.47659416437845764
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo2Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 0.9999999999999999 0.476594164378458
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -0.7949518201966582
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo3Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.11459511313577637 -0.02276732956873983 -0.9931513523877956 0.7998692107708487
                                children [
                                  DEF ee_backLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(6)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF staticBody Solid {
      children [
        DEF mainBody Shape {
          appearance Asphalt {
          }
          geometry Box {
            size 0.079 0.2 0.01
          }
          castShadows FALSE
        }
        DEF middleLegOffset Shape {
          appearance Asphalt {
          }
          geometry Box {
            size 0.129 0.01 0.01
          }
          castShadows FALSE
        }
      ]
      boundingObject USE middleLegOffset
      physics Physics {
      }
    }
  ]
  name "robot(1)"
  boundingObject USE mainBody
  physics Physics {
  }
  controller "walkingController"
  supervisor TRUE
}
'''

preamble = '''#VRML_SIM R2023b utf8

EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackground.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/backgrounds/protos/TexturedBackgroundLight.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/objects/floors/protos/RectangleArena.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/ReflectiveSurface.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/DamascusSteel.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/SolarCell.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/Asphalt.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/GlossyPaint.proto"
EXTERNPROTO "https://raw.githubusercontent.com/cyberbotics/webots/R2023b/projects/appearances/protos/FormedConcrete.proto"

WorldInfo {
    basicTimeStep 50
}
Viewpoint {
    orientation -0.33927166805244596 0.3526814749301854 0.8720725385528314 1.6687661308506603
position -0.28940393845342743 -3.058024758031703 3.795574343577446
}
TexturedBackground {
}
TexturedBackgroundLight {
}
RectangleArena {
    floorSize 10 10
floorTileSize 1 1
floorAppearance FormedConcrete {
}
}
DEF finishLine Pose {
    translation 0 3 0
children [
    Shape {
    geometry Box {
    size 10 0.01 0.001
}
}
]
}
DEF dhExpectation Pose {
    translation -1 0 0
children [
    Shape {
    geometry Box {
    size 0.01 10 0.001
}
}
]
}
DEF uninjuredExpectation Shape {
    geometry Box {
    size 0.01 10 0.001
}
}'''

uninjuredRobot = '''
DEF robot Robot {
  translation 0 0 0.1
  children [
    DEF frontRightLeg Solid {
      translation 0.0585 0.1195 0
      rotation 0 0 -1 0.785398
      children [
        DEF r_frontRightLeg Solid {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position 0.4418089277882036
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo16Motor"
            }
          ]
          endPoint Solid {
            translation -4.402082242754249e-05 -2.7660386327051132e-06 -1.139528764265707e-06
            rotation -0.00010523333265663223 6.229772278563197e-05 0.9999999925224698 0.4418395772029311
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 -1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position 0.2153419495114004
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo17Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 -1 0.21534194951139976
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          rotation 0 1 0 ''' + str(frontRightS3_twistRadians) + '''
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position 0.34788423834320353
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo18Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation 0 0 1 0.34788423834320376
                                children [
                                  DEF ee_frontRightLeg Solid {
                                    translation -0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation -0.0505 0.0455 0
                                    rotation 0 0 -1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(2)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF middleRightLeg Solid {
      translation 0.092 0 0
      rotation 0 0 -1 1.5708
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.15294251470290374
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo13Motor"
            }
          ]
          endPoint Solid {
            translation 1.4720633054250261e-05 2.21178361829653e-05 4.1781194690948525e-06
            rotation 6.901659850513326e-06 -7.2888532550347e-07 -0.9999999999759179 0.15294251480503496
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 -1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position 0.5025723256897849
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo14Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 -1 0.5025723256897852
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position 0.8535074025393279
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo15Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation 0 0 0.9999999999999999 0.8535074025393281
                                children [
                                  DEF ee_middleRightLeg Solid {
                                    translation -0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation -0.0505 0.0455 0
                                    rotation 0 0 -1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(3)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF backRightLeg Solid {
      translation 0.0585 -0.1195 0
      rotation 0 0 -1 2.35619449
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position 0.5405189658225488
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo10Motor"
            }
          ]
          endPoint Solid {
            translation 9.010419606852597e-06 7.56383763510589e-05 9.003554777564646e-07
            rotation -7.49040793252198e-05 -9.904665055189473e-05 0.9999999922895699 0.5405106498450373
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 -1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position 0.5678646331727851
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo11Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 -1 0.5678646331727851
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position 1.01280932112563
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo12Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation 0 0 1 1.01280932112563
                                children [
                                  DEF ee_backRightLeg Solid {
                                    translation -0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation -0.0505 0.0455 0
                                    rotation 0 0 -1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(4)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF frontLeftLeg Solid {
      translation -0.0585 0.1195 0
      rotation 0 0 1 0.7853980000000005
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position 0.5328777222685075
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo7Motor"
            }
          ]
          endPoint Solid {
            translation 1.4904981469858678e-05 5.9737751574990734e-05 3.0576497142553727e-07
            rotation 1.4159206830996164e-06 1.6068906353561518e-07 0.9999999999989847 0.5328777223190871
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.5677889397429712
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo8Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 0.9999999999999999 0.5677889397429714
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -1.012767157030366
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo9Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.093122426135155 -0.008142304178925102 -0.9956213721256493 1.0164940240044722
                                children [
                                  DEF ee_frontLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(1)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF middleLeftLeg Solid {
      translation -0.092 0 0
      rotation 0 0 1 1.570796327
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.15989029731818805
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo4Motor"
            }
          ]
          endPoint Solid {
            translation 1.2580745632270811e-05 1.893438732529186e-05 -1.2476656639781591e-06
            rotation 1.603781940526206e-06 6.543934278725805e-08 -0.9999999999987118 0.15989029740209343
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.5025148304221267
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo5Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 1 0.5025148304221271
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -0.8534667000017102
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo6Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.10784243399679382 -0.018164025112173673 -0.9940020511152738 0.8580091073744344
                                children [
                                  DEF ee_middleLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(5)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF backLeftLeg Solid {
      translation -0.0585 -0.1195 0
      rotation 0 0 1 2.35619449
      children [
        DEF r Pose {
          translation 0 -0.027 0
          children [
            Shape {
              appearance GlossyPaint {
                baseColor 1 0 0
              }
              geometry Box {
                size 0.01 0.01 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF r_s1 Pose {
          translation 0 -0.015 0
          children [
            Shape {
              appearance SolarCell {
              }
              geometry Box {
                size 0.01 0.027 0.01
              }
              castShadows FALSE
            }
          ]
        }
        DEF servo1 HingeJoint {
          jointParameters HingeJointParameters {
            position -0.24285815711096004
            axis 0 0 1
          }
          device [
            RotationalMotor {
              name "servo1Motor"
            }
          ]
          endPoint Solid {
            translation -3.1632268366720574e-05 3.290628735984607e-05 2.3429621350545818e-06
            rotation 2.8737755961297603e-06 1.3880855935554242e-07 -0.9999999999958611 0.24285815706879205
            children [
              DEF s2 Solid {
                translation 0 0.044 0
                rotation 0 1 0 1.570796327
                children [
                  DEF servo2 HingeJoint {
                    jointParameters HingeJointParameters {
                      position -0.4765939388262514
                      axis 0 0 -1
                    }
                    device [
                      RotationalMotor {
                        name "servo2Motor"
                      }
                    ]
                    endPoint Solid {
                      rotation 0 0 1 0.4765939388262513
                      children [
                        DEF s3 Solid {
                          translation 0 0.075 0
                          children [
                            DEF servo3 HingeJoint {
                              jointParameters HingeJointParameters {
                                position -0.7949515211911659
                                axis 0 0 1
                              }
                              device [
                                RotationalMotor {
                                  name "servo3Motor"
                                }
                              ]
                              endPoint Solid {
                                rotation -0.11459514998349328 -0.022767354698047103 -0.9931513475600352 0.7998689138131404
                                children [
                                  DEF ee_backLeftLeg Solid {
                                    translation 0.101 0.091 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF endEffector Shape {
                                        appearance DamascusSteel {
                                        }
                                        geometry Sphere {
                                          radius 0.005
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                    boundingObject USE endEffector
                                    physics Physics {
                                    }
                                  }
                                  DEF s3_ee Pose {
                                    translation 0.0505 0.0455 0
                                    rotation 0 0 1 0.733361849
                                    children [
                                      DEF s3_eeShape Shape {
                                        appearance SolarCell {
                                        }
                                        geometry Box {
                                          size 0.13 0.01 0.01
                                        }
                                        castShadows FALSE
                                      }
                                    ]
                                  }
                                ]
                                boundingObject USE s3_eeShape
                                physics Physics {
                                }
                              }
                            }
                            DEF servo3Shape Shape {
                              appearance ReflectiveSurface {
                              }
                              geometry Cylinder {
                                height 0.01
                                radius 0.005
                              }
                              castShadows FALSE
                            }
                          ]
                          boundingObject USE servo3Shape
                          physics Physics {
                          }
                        }
                        DEF s2_s3 Pose {
                          translation 0 0.0375 0
                          children [
                            DEF s2_s3Shape Shape {
                              appearance SolarCell {
                              }
                              geometry Box {
                                size 0.01 0.07 0.01
                              }
                              castShadows FALSE
                            }
                          ]
                        }
                      ]
                      boundingObject USE s2_s3Shape
                      physics Physics {
                      }
                    }
                  }
                  DEF servo2Shape Shape {
                    appearance ReflectiveSurface {
                    }
                    geometry Cylinder {
                      height 0.01
                      radius 0.005
                    }
                    castShadows FALSE
                  }
                ]
                boundingObject USE servo2Shape
                physics Physics {
                }
              }
              DEF servo1Shape Shape {
                appearance ReflectiveSurface {
                }
                geometry Cylinder {
                  height 0.01
                  radius 0.005
                }
                castShadows FALSE
              }
              DEF s1_s2 Pose {
                translation 0 0.022 0
                children [
                  DEF s1_s2Shape Shape {
                    appearance SolarCell {
                    }
                    geometry Box {
                      size 0.01 0.04 0.01
                    }
                    castShadows FALSE
                  }
                ]
              }
            ]
            name "solid(1)"
            boundingObject USE s1_s2Shape
            physics Physics {
            }
          }
        }
      ]
      name "solid(6)"
      boundingObject USE servo1Shape
      physics Physics {
      }
    }
    DEF staticBody Solid {
      children [
        DEF mainBody Shape {
          appearance Asphalt {
          }
          geometry Box {
            size 0.079 0.2 0.01
          }
          castShadows FALSE
        }
        DEF middleLegOffset Shape {
          appearance Asphalt {
          }
          geometry Box {
            size 0.129 0.01 0.01
          }
          castShadows FALSE
        }
      ]
      boundingObject USE middleLegOffset
      physics Physics {
      }
    }
  ]
  boundingObject USE mainBody
  physics Physics {
  }
  controller "walkingController"
  supervisor TRUE
}'''

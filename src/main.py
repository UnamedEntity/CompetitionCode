import sys 
import vex
from vex import *
import math

brain = vex.Brain()
frontLeftMotor = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO_18_1, False)
frontRightMotor = vex.Motor(vex.Ports.PORT19, vex.GearSetting.RATIO_18_1, True)
backLeftMotor = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO_18_1, False)
backRightMotor = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO_18_1, True)
controller = vex.Controller(vex.ControllerType.PRIMARY)

def xDrive(forward, strafe, turn, direction):
    fl = forward + strafe + turn
    fr = forward - strafe - turn
    bl = forward - strafe + turn
    br = forward + strafe - turn
    frontLeftMotor.spin(direction, fl, vex.VelocityUnits.PERCENT)
    frontRightMotor.spin(direction, fr, vex.VelocityUnits.PERCENT)
    backLeftMotor.spin(direction, bl, vex.VelocityUnits.PERCENT)
    backRightMotor.spin(direction, br, vex.VelocityUnits.PERCENT)




while True:
    forward = controller.axis3.value() 
    strafe = controller.axis4.value()  
    turn = controller.axis1.value()
    xDrive(forward, strafe, turn, vex.DirectionType.FORWARD)


        

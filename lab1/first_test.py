#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:50:16 2018

@author: u5869920
"""
import robot
robot.init() # the default gripper mode is folded 
             # init(ip_address = None, visualise = True, width = 5, height = 2,
             # pos = -1, boxes = [["red"], [], ["green"], [], ["blue"]])
def drive_right_twice():     
    robot.drive_right()
    robot.drive_right()

def drive_left_twice():
    robot.drive_left()
    robot.drive_left()

def grab_up_cube():
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_closed()

def grab_bottom_cube():
    robot.gripper_to_open()
    robot.lift_down()
    robot.gripper_to_closed()
  
def swap_two_close():
    robot.lift_up()
    drive_right_twice()
    grab_bottom_cube()
    drive_left_twice()
    grab_up_cube()
    drive_right_twice()
    robot.lift_down()
        
def swap_left_and_middle():
    robot.drive_right()
    robot.lift_up()
    grab_bottom_cube()
    swap_two_close()

#swap_left_and_middle()
   
def swap_middle_and_right():
    drive_right_twice()
    swap_left_and_middle()
    
#swap_middle_and_right()
    
def swap_left_and_right():
    swap_left_and_middle()
    swap_two_close()
    robot.gripper_to_open()
    robot.lift_up()
    robot.gripper_to_folded()
    robot.lift_down()
    drive_left_twice()
    drive_left_twice()
    robot.drive_left()
    swap_left_and_middle()
    
#swap_left_and_right()   

    
    
    
    
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:46:59 2022

@author: spike
"""
from state_machine import Section

if __name__ == "__main__":
    
    first_section=Section()
    world_state=first_section.state
    first_section.show_frame()
    first_section.show_state()
    first_section.show_diff(world_state,[],0)
    first_section.dump_json()
    

    first_section.add_action('ptr',["get_up","climbing_towards_the_cave_entrance"])
    first_section.show_frame()
    first_section.show_diff(world_state,[],0)
    first_section.update_old_state()
    first_section.dump_json()
    
    first_section.add_feeling('ptr',["blind","fresh_air"])
    first_section.add_action('ptr',["raised_arm_to_block_the_sudden_light_from_outsidey"])
    first_section.show_frame()
    first_section.show_diff(world_state,[],0)
    first_section.update_old_state()
    first_section.dump_json()
    
    first_section.change_location("at_the_bottom_of_the_sinkhole")
    first_section.add_thought('ptr',["where_am_i_?"])
    first_section.show_frame()
    first_section.show_diff(world_state,[],0)
    first_section.update_old_state()
    first_section.dump_json()
    
    first_section.show_story()
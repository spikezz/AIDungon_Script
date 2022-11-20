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
    
    first_section.add_feeling('ptr',["blind","fresh_air","cold","confused"])
    first_section.add_action('ptr',["raised_arm_to_block_the_sudden_light_from_outside"])
    first_section.add_thought('ptr',["where_am_i_?"])
    first_section.show_frame()
    first_section.show_diff(world_state,[],0)
    first_section.update_old_state()
    first_section.dump_json()
    
    first_section.change_location("at_the_bottom_of_the_sinkhole",["fresh_air","cold"])
    first_section.show_frame()
    first_section.add_action('ptr',["walk_outside"])
    first_section.add_feeling('ptr',["cold","weak"])
    first_section.show_diff(world_state,[],0)
    first_section.update_old_state()
    first_section.dump_json()
    
    # first_section.show_frame()
    # first_section.add_action('ptr',["stumbling_forward"])
    
        
    
    # 小女孩的居住地，
    # 小女孩设定： 
    #   看起来像是男孩，短金发，瘦小，眸子很亮，单纯，爽利。穿着兽皮
    first_section.show_story()
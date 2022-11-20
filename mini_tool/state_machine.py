# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:14:07 2022

@author: spike
"""
import os
import json
import pathlib
from collections  import defaultdict
from pprint import pprint
from copy import deepcopy

def get_location_template(location):
    
    location_template_dict=defaultdict(lambda: {})
    location_template_dict[location]={}
    location_template_dict[location]['env_state']={}
    location_template_dict[location]['env_state']['human_feeling']=[]
    location_template_dict[location]['items']=[]
    
    return dict(location_template_dict)


class Section:
    
    def __init__(self):
        self.story_dir=pathlib.Path().resolve()/"story.json"
        if os.path.exists(self.story_dir):
          os.remove(self.story_dir)
        else:
          print("Story does not exist")
        with open(self.story_dir,'w') as f:
            json.dump({}, f)

        self.timeline={}
        
        self.frame=0
        
        # world state init
        self.state=defaultdict(lambda: {})

        #main camera
        self.state['characters']['ptr']={}
        ptr=self.state['characters']['ptr']
        ptr['appearence']=["AnimalSkin"]
        ptr['behavior']=["wake_up", "sit_up","head_up_look_at_the_entrance_of_the_cave"]
        ptr['feeling']=[]
        ptr['thought']=[]
        
        #start location
        location=get_location_template("cave")
        location['cave']['env_state']['human_feeling']=["warm","dark"]
        location['cave']['items']=["StrawMat","Campfire"]
        self.state['location']=location
        
        self.old_state=deepcopy(self.state)
        
    def show_frame(self):
        print("frame: ",self.frame)
        
    def show_state(self):
        pprint(dict(self.state))
    
    def show_diff(self,new_state,path,depth):
        for k, v in new_state.items():
            # print(v)
            depth+=1
            if isinstance(v, dict):
                path.append(k)
   
                self.show_diff(v,path,depth)
                depth-=1
                path.pop(-1)
            else:
                cmd="self.state"
                cmd_old_parent="self.old_state"
                cmd_old="self.old_state"
                exsit_in_old_state=True
                for key in path:
                    if key in eval(cmd_old_parent):
                        cmd_old_parent+="['"+key+"']"
                    else:
                        exsit_in_old_state=False
                        break
                # print(exsit_in_old_state)
                if exsit_in_old_state:
                    path.append(k)
                    for key in path:
                        cmd+="['"+key+"']"
                        cmd_old+="['"+key+"']"
                    # print("check: ",path,cmd,cmd_old)
                    if eval(cmd)!=eval(cmd_old):
                        for x in eval(cmd):
                            if x not in eval(cmd_old):
                                print(f"{path} new {k}: ",x)
                    path.pop(-1)
                else:
                    for key in path:
                        cmd+="['"+key+"']"
                    print(f"new ",cmd,": ",eval(cmd))

    def update_old_state(self):
        self.old_state=deepcopy(self.state)
    
    def dump_json(self):
        with open (self.story_dir,"r") as j_file:
            data=json.load(j_file)
        data[self.frame]=self.state
        with open (self.story_dir,"w") as j_file:
            json.dump(data, j_file)
        self.frame+=1
    
    def show_story(self):
        with open (self.story_dir,"r") as j_file:
            data=json.load(j_file)
            print("\nfull history: \n")
            pprint(data)
    
    def add_action(self,character,action):
        self.state['characters'][character]['behavior']+=action
    
    def add_thought(self,character,thought):
        self.state['characters'][character]['thought']+=thought
    
    def add_feeling(self,character,feeling):
        self.state['characters'][character]['feeling']+=feeling
    
    def change_location(self,location,human_feeling=None):
        self.state['location'].update(get_location_template(location))
        if human_feeling:
            self.state['location'][location]['env_state']['human_feeling']+=human_feeling
        
if __name__ == "__main__":
    
    first_section=Section()
    first_section.show_story()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
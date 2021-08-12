import json
from pprint import pprint

class world_generator(object):

    def __init__(self,input_file_path,output_file_path):

        self.input_file_path=input_file_path
        self.output_file_path=output_file_path
        
    def load_world_info(self):

        with open(self.input_file_path) as json_file:
            self.world_info = json.load(json_file)
            print(self.world_info[0])

    def organize_world_info_structure(self):

        print(f"library volum:{len(self.world_info)}")
        keyset=set()
        self.world_info_dict={"summary":{}}
        null = None
        for idx,entity in enumerate(self.world_info):

            if entity['type'] not in self.world_info_dict['summary']:
                self.world_info_dict['summary'][entity['type']]=[]
            self.world_info_dict['summary'][entity['type']].append(entity['name'])

            if entity['keys']==null:
                print(entity['name'])
                self.world_info[idx]['keys']=entity['name']

            keyset.update(list(entity.keys()))

        pprint(f"keyset:{keyset}")
        pprint(f"world_info_dict\n{self.world_info_dict}")
        self.dump_statistic()

    def dump_statistic(self):
        
        with open(self.output_file_path,'w',encoding='utf-8') as json_file:
            json.dump(self.world_info_dict, json_file, ensure_ascii=False,indent=4)
        with open(self.input_file_path,'w',encoding='utf-8') as json_file:
            json.dump(self.world_info, json_file, ensure_ascii=False,indent=2)
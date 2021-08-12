import world_generator

if __name__ == '__main__':
    
    input_file_path="D:\Project\AIDungon_Script\mini_tool\worldInfo.json"
    output_file_path="D:\Project\AIDungon_Script\mini_tool\statistic.json"
    gen=world_generator.world_generator(input_file_path,output_file_path)
    gen.load_world_info()
    gen.organize_world_info_structure()
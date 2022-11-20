# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 23:57:46 2022

@author: spike
"""

import pathlib
from collections  import defaultdict,OrderedDict
from pprint import pprint

def load_prompt_data(prompt_data_path):
    with open(prompt_data_path,'r') as prompt_data_file:
        return prompt_data_file.readlines()

def translate_prompt(word):
    word=word.replace("聽", " ")
    if "{" in word:
        big_brakets_count=word.count("{")
        word_kern=word.strip().strip("{}")
        new_weight=pow(1.05,big_brakets_count)
        new_word=f"({word_kern}:{new_weight})"
        return new_word,word_kern,new_weight
    elif "(" in word:
        brakets_count=word.count("(")
        word_kern=word.strip().strip("()")
        new_weight=pow(1.1,brakets_count)
        new_word=f"({word_kern}:{new_weight})"
        # print(brakets_count,word_kern,new_weight,new_word)
        return new_word,word_kern,new_weight
    else:
        return word.strip(),word.strip(),1

def rebuild_prompt_and_build_statistic(lines):
    statistic=defaultdict(lambda: defaultdict(lambda: 0))
    new_file=[]
    for line in lines:
        words=line.split(",")
        words[-1]=words[-1].strip("\n")
        new_line=""
        for i,word in enumerate(words):
            words[i],word_kern,weight=translate_prompt(word)
            new_line+=words[i]+", "
            statistic[word_kern][weight]+=1
        new_file.append(new_line[:-2])
    for k,v in statistic.items():
        statistic[k]=dict(OrderedDict(sorted(v.items())))
    statistic=OrderedDict(sorted(statistic.items()))
    pprint(statistic)
    pprint(new_file)
    return new_file,statistic

def dump_translated_prompt(new_prompt_file,prompt_data_path):
    with open(prompt_data_path,'w') as prompt_data_file:
        for line in new_prompt_file:
            prompt_data_file.write(f"{line}\n")
    
if __name__ == "__main__":
    
    print("positive prompt: ")
    positive_prompt_data_path=pathlib.Path().resolve()/"positive_prompt_data.txt"
    new_positive_prompt_file,positive_prompt_statistic=rebuild_prompt_and_build_statistic(load_prompt_data(positive_prompt_data_path))
    
    new_positive_prompt_data_path=pathlib.Path().resolve()/"new_positive_prompt_data.txt"
    dump_translated_prompt(new_positive_prompt_file,new_positive_prompt_data_path)
    
    print("\n")
    
    print("negative prompt: ")
    negative_prompt_data_path=pathlib.Path().resolve()/"negative_prompt_data.txt"
    new_negative_prompt_file,negative_prompt_statistic = rebuild_prompt_and_build_statistic(load_prompt_data(negative_prompt_data_path))
    
    new_negative_prompt_data_path=pathlib.Path().resolve()/"new_negative_prompt_data.txt"
    dump_translated_prompt(new_negative_prompt_file,new_negative_prompt_data_path)
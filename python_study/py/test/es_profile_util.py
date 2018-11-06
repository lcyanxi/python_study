#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/5 18:33
# @Author  : lcyanxi
# @Email   : lcyanxi.com
# @File    : es_profile_util.py
# @Software: PyCharm

import collections
import json

# 用户画像工具类数据转换工具
# eg: string:imeilong:user_idlong:heightstring:aimArray:interested_tags-tagArray:taboos_id-id
# 00000000江苏苏州女60后学生["酸甜","汤","清淡","养颜","煮妇","宝宝餐","养生","素食","食疗","健身","家常","减肥"]
# {"imei": "00000000", "user_id": "", "user_name": "", "nickname": "", "province": "广东", "city": "深圳", "sex": "女"}


if __name__ == "__main__":

    flag = True
    title_list = []
    f = open("D:/result.log", "w", encoding="utf-8")
    with open("D:/temp.log", "r", encoding="utf-8") as fr:
        for line in fr:
            words = line.strip().split("")
            # 处理表头
            if flag:
                flag = False
                for word in words:
                    title_dict = {}
                    title_type = word.split(":")[0]
                    title_value = word.split(":")[1]
                    title_dict["type"] = title_type
                    title_dict["name"] = title_value
                    # 处理数组类型字段
                    if title_type == "Array":
                        title_dict["name"] = title_value.split("-")[0]
                        title_dict["sub_name"] = title_value.split("-")[1]
                    title_list.append(title_dict)
            # 处理内容
            else:
                if len(words) == len(title_list):
                    index = 0
                    result_dict = collections.OrderedDict()
                    for target in words:
                        title_type = title_list[index]["type"]
                        title_name = title_list[index]["name"]
                        # 判断是否是数组数据
                        if title_type == "Array":
                            sub_list = []
                            title_sub_name = title_list[index]["sub_name"]
                            if target != "":
                                new_target = target.replace("[\"", "").replace("\"]", "").replace("\"", "")
                                for tmp in new_target.split(","):
                                    sub_dict = {}
                                    sub_dict[title_sub_name] = tmp
                                    sub_list.append(sub_dict)
                                result_dict[title_name] = sub_list
                            else:
                                result_dict[title_name] = ""
                        else:
                            result_dict[title_name] = target

                        index += 1
                    my_json = json.dumps(result_dict, ensure_ascii=False)
                    f.writelines(my_json + "\n")
    print(str(title_list))
    f.close()

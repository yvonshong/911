import json

if __name__ == "__main__":

    f_txt = open("txt.txt")               # 返回一个文件对象   
    line = f_txt.readline()
    block_str = ""

    block_id = 0
    cnt = 0
    while line:   
        cnt += 1
        # if cnt > 20:
        #     break
        line = f_txt.readline() 
        print(line)  
        block_str = line
        block_dict = {}
        block_dict["data"] = [block_str]
        with open(f"data/{block_id}.json",'w',encoding='utf-8') as f_block:
            json.dump(block_dict, f_block, ensure_ascii=False)
        block_id+=1
    
    f_txt.close() 
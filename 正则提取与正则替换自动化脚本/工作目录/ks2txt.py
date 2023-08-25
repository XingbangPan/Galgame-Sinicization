import os

targetDir = r'script_jp'
files =  os.listdir(targetDir)
for file in files:
    filename=file.replace(".ks",".json")

    #打开并读取script_jp内容
    with open("script_jp\\"+file,'r',encoding='utf-16') as f:
        text=f.read()

    #正则匹配模式
    import re
    p=re.compile('^\[blink.*?text="(.*?)".*?\]$',re.MULTILINE)
    if len(p.findall(text))==0:print("列表为空")
    else:
        #创建并写入匹配内容到json_jp
        with open("json_jp\\"+filename,'w',encoding='utf-8') as f:
            f.write("[\n")
            for one in p.findall(text):
                f.write("  {\n    \"message\": \"")
                f.write(one)
                f.write("\"\n  },\n")
            f.seek(f.tell() - 3, 0)
            f.truncate()
            f.write("\n]")
      







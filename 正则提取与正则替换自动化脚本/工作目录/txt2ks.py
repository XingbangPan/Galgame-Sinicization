import os
targetDir = r'json_cn'
files =  os.listdir(targetDir)
for file in files:
    filename=file.replace(".json",".ks")
    #读取json_cn 中文选项
    with open("json_cn\\"+file,'r',encoding='utf-8') as f:
        choiceText=f.read()
        import re
        p=re.compile(': "(.*?)"')
        choices=re.findall(p,choiceText)
        print(choices)

    #读取源文本
    with open("script_jp\\"+filename,'r',encoding='utf-16') as f:
        text=f.read()

    #匹配模式替换帮助函数
    def func(match):
        global i
        result= match[1]+choices[i]+match[3]
        i=i+1
        return result
    i=0

    #匹配模式替换
    import re
    p=re.compile('(^\[blink.*?text=")(.*?)(".*?\]$)',re.MULTILINE)
    newText=re.sub(p,func,text)
    print(newText)

    #创建并将已替换文本写入script_cn
    with open("script_cn\\"+filename,'w',encoding='utf-16') as f:
        f.write(newText)


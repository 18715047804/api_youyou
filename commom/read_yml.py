import yaml
import os

def readyml(yamlPath):
    """读取yaml文件内容"""
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件不存在")
    f = open(yamlPath, 'r', encoding="utf-8")
    c = f.read()
    # 转python dict list
    d = yaml.safe_load(c)
    print("读取的文件数据：", d)
    return d
if __name__ == '__main__':
    path = r"C:\Users\yangfei\Desktop\yoyo_api_preject\data\data.yaml"
    readyml(path)
import os

# 创建文件夹
for i in range(1, 16):
    folder_name = f"folder_{i}"
    os.makedirs(folder_name)


# 创建Python文件
for i in range(1, 16):
    file_name = f"file_{i}.py"
    with open(file_name, "w") as file:
        file.write("# 这是一个Python文件")

print("文件夹和文件创建完成！")


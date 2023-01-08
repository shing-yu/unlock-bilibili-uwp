import sys

if len(sys.argv) < 2:
    file = input('请输入文件名/路径(可直接拖入文件):\n(也可将文件拖动到exe文件上解密):\n')
else:
    file = sys.argv[1]
out_fnh = input('请输入解密后文件名:\n')
# 读取文件数据
with open(file, "rb") as f:
    data = f.read()

# 删除开头的 FF FF FF 字节
decrypted_data = data[3:]

# 创建新文件并写入解密后的数据
with open(f"{out_fnh}.mp4", "wb") as f:
    f.write(decrypted_data)

# 关闭文件
f.close()

import shutil
import os
import datetime
import tarfile

def backup_and_compress(source, destination):
    try:
        # 检查源文件或文件夹是否存在
        if os.path.exists(source):
            # 检查目标目录是否存在，如果不存在则创建
            if not os.path.exists(destination):
                os.makedirs(destination)
            
            # 生成备份文件名，加上当前日期时间
            backup_filename = os.path.basename(source) + '-' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.tar.gz'
            
            # 构建备份路径
            backup_path = os.path.join(destination, backup_filename)
            
            # 创建压缩文件
            with tarfile.open(backup_path, "w:gz") as tar:
                # 将源文件或文件夹添加到压缩文件中
                tar.add(source, arcname=os.path.basename(source))
            
            print("恭喜备份并压缩成功！备份文件路径：", backup_path)
            
            # 添加自定义信息输出
            print("脚本由阿鱼君编写维护ayujun@hotmail.com")
        else:
            print("源文件或文件夹不存在！")
    except Exception as e:
        print("抱歉备份失败：", str(e))

# 请修改以下两行为你自己的备份源文件或文件夹路径和备份目标路径
source_path = "你的数据目录"
backup_destination = "备份数据存放的目录"

# 执行备份和压缩
backup_and_compress(source_path, backup_destination)

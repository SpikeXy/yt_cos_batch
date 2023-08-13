import sys
import os
import logging
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos.cos_exception import CosClientError, CosServiceError
import subprocess

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = ''    # 设置用户的secret_id和secret_key
secret_key = ''   # 设置用户的secret_id和secret_key
region = ''   # bucket区域名称
bucket_name = ''    # bucket名称
folder_name = '' # cos存储的根目录的文件夹名称     

token = None               
scheme = 'https'          


config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)



# 使用youtube-dl下载单个视频
def upload():
    # 上传到腾讯云
    print("开始上传文件：")
    for root, dirs, files in os.walk('./'):
        for file in files:  
            if file.count('.mp4') == 1 or file.count('vtt')  or file.count('m4a') == 1:
                print("开始上传文件：", file)
                file_path = os.path.join(root, file)
                upload_file_path = folder_name+ file
                response = client.upload_file(
                    Bucket=bucket_name,
                    Key= upload_file_path,
                    LocalFilePath= file_path,
                    EnableMD5=False,
                    progress_callback=None
                )

                # 上传完成后删除本地文件
                os.remove(file_path)
            else:
                print("其他文件跳过")

if __name__ == '__main__':
    upload()
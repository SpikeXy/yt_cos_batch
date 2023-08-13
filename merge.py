import os
import subprocess

def video_add_audio(video_file, audio_file, file_name):
    """
     视频添加音频
    :param file_name: 传入视频文件的路径
    :param mp3_file: 传入音频文件的路径
    :return:
    """
    # outfile_name = file_name + '-txt.mp4'
    process  = subprocess.Popen('ffmpeg -i ' + video_file
                    + ' -i ' + audio_file + ' -strict -2 -f mp4 '
                    + file_name, shell=True)
    # return process
    process.wait()

def process_files(files):
    p_list = []
    for file in files:
        if file.endswith('.mp4'):
            file_name = file[:-4]
            file_new_name = file[:-4]
            if(file_name.find(' ') != -1):
                file_new_name = file_name.replace(' ','-')
            
            file_mp4_path =  os.path.join(resource_dir , file_name + '.mp4')
            file_audio_path = os.path.join(m4a_dir , file_name + '.m4a')

            # 查找一下file_audio_path是否存在
            if(not os.path.exists(file_audio_path)):
                print('音频文件不存在：' + file_audio_path)
                continue

            # 新的最终文件路径
            file_final_path = os.path.join(new_dir, file_new_name+'.mp4')
            # 确定新的文件是否已经生成
            if(os.path.exists(file_final_path)):
                print('已经存在：' + file_new_name)
                continue
            else:
                # 重命名
                file_mp4_new_path = os.path.join(resource_dir , file_new_name + '.mp4')
                file_audio_new_path = os.path.join(m4a_dir , file_new_name + '.m4a')
                os.rename(file_mp4_path,file_mp4_new_path)
                os.rename(file_audio_path,file_audio_new_path)
                video_add_audio(file_mp4_new_path,file_audio_new_path,file_final_path)
                print('合成完成：' + file_new_name)


root=r'D:\video\ocmp4合成'
new_dir =  os.path.join(root, 'new_mp4').replace('\\','/')
resource_dir = os.path.join(root, 'mp4').replace('\\','/')
m4a_dir = os.path.join(root, 'm4a').replace('\\','/')

if __name__ == '__main__':

    # 将文件夹下的所有文件名添加到一个列表
    files = os.listdir(resource_dir)
    process_files(files)
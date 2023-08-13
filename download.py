import sys
import os
import logging
import subprocess
import concurrent.futures


# 251          webm       audio only tiny   46k , webm_dash container, opus @ 46k (48000Hz), 7.32MiB
# 140          m4a        audio only tiny  129k , m4a_dash container, mp4a.40.2@129k (44100Hz), 20.51MiB
# 160          mp4        256x144    144p   18k , mp4_dash container, avc1.4d400c@  18k, 30fps, video only, 2.91MiB
# 243          webm       640x360    360p   54k , webm_dash container, vp9@  54k, 30fps, video only, 8.68MiB
# 134          mp4        640x360    360p   60k , mp4_dash container, avc1.4d401e@  60k, 30fps, video only, 9.64MiB
# 136          mp4        1280x720   720p  167k , mp4_dash container, avc1.64001f@ 167k, 30fps, video only, 26.58MiB
# 137          mp4        1920x1080  1080p  309k , mp4_dash container, avc1.640028@ 309k, 30fps, video only, 49.02MiB
# 18           mp4        640x360    360p  153k , avc1.42001E, 30fps, mp4a.40.2 (44100Hz), 24.35MiB
# 22           mp4        1280x720   720p  296k , avc1.64001F, 30fps, mp4a.40.2 (44100Hz) (best)

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
       
# 使用youtube-dl下载单个视频
def download(url):

    
    # cmd = f'python -m youtube_dl -x  {url} --verbose '  # 只下载m4a音频
    cmd = f'python -m youtube_dl -f 136 {url} --verbose ' # 只下载视频

    completed_process = subprocess.run(cmd, shell=True, capture_output=False)

    # 检查命令是否成功执行
    if completed_process.returncode == 0:
        print("命令执行成功")
    else:
        print("命令执行失败")

if __name__ == '__main__':

    url_list = []
    # 读取links.txt文件，下载视频
    with open('links.txt', 'r') as f:
        url_list_temp = f.readlines()
        for url in url_list_temp:
            # 如果url包含[ 或者 ]，则跳过
            if '[' in url or ']' in url:
                continue
            else:
                real_url = 'https://www.youtube.com'+  url.replace(',', '').replace('\"', '').strip()
                url_list.append(real_url)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(download, url_list)
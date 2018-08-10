#!/usr/env python

# by LoopGod

from subprocess import Popen, PIPE
import time,os
import subprocess

#ffmpeg -ss 00:00:00 -i oldvideo.mp4 -c copy -t 60 2.mp4
class Shell(object) :
  def runCmd(self, cmd) :
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sout ,serr = res.communicate()   
    return res.returncode, sout, serr, res.pid

def cut(shell):
  print ("===退出程序输入exit或者bye即可 (阿玲专属程序-LG)===")
  mypathlist = os.getcwd().split('\\')#input('输入视频路径,ex: F:/cut_Video_python \n>>>').split('\\')
  if len(mypathlist)==1:
    mypath=mypathlist[0]
  else:
    mypath='/'.join(mypathlist)
  input0 = "cd "+mypath
  if input0 == 'cd exit' or input0 == 'cd bye' :
    return -1
  else :
    result = shell.runCmd(input0)

  oldvideo = input('输入视频全称,ex: oldvideo.mp4 \n>>>')  
  if oldvideo == 'exit' or oldvideo == 'bye' :
    return -1
  starttime = input('输入起始时间,ex: hh:mm:ss \n>>>')
  if starttime == 'exit' or starttime == 'bye' :
    return -1
  endtime = input('输入结束时间,ex: hh:mm:ss \n>>>')
  if endtime == 'exit' or endtime == 'bye' :
    return -1
  newvideo = input('输入新视频全称,ex: newvideo.mp4 \n>>>')
  if newvideo == 'exit' or newvideo == 'bye' :
    return -1
  input1="ffmpeg -ss {st} -i {ov} -c copy -t {et} {ev}".format(st=starttime,ov=oldvideo,et=endtime,ev=newvideo)
  result = shell.runCmd(input1)
  if result[2]==None:
    print("cut success!!!\n")


def join(shell):
  print ("===退出程序输入exit或者bye即可 (阿玲专属程序-LG)===")
  mypathlist = os.getcwd().split('\\')#input('输入视频路径,ex: F:/cut_Video_python \n>>>').split('\\')
  if len(mypathlist)==1:
    mypath=mypathlist[0]
  else:
    mypath='/'.join(mypathlist)
  input0 = "cd "+mypath
  if input0 == 'cd exit' or input0 == 'cd bye' :
    return -1
  else :
    result = shell.runCmd(input0)

  video1 = input(
      "Enter your first video file name. ex: firstVideo.mp4\n>>>")
  tmp1 = video1 + "tmp.mpg"
  if tmp1 == 'exit' or tmp1 == 'bye' :
    return -1
  video2 = input(
      "Enter your second video file name. ex: secondVideo.mp4\n>>>")
  tmp2 = video2 + "tmp.mpg"
  if video2 == 'exit' or video2 == 'bye' :
    return -1
  finalVideo = input("Enter new video file name. ex: myNewVideo.mp4\n>>>")
  tmpout = video1 + video2 + "tmp.mpg"
  if finalVideo == 'exit' or finalVideo == 'bye' :
    return -1
  cmd1 = 'ffmpeg -i {vi1} -qscale:v 1 {t1}'.format(vi1=video1,t1=tmp1)
  cmd2 = 'ffmpeg -i {vi2} -qscale:v 1 {t2}'.format(vi2=video2,t2=tmp2)
  conc = '"'+'concat:' + tmp1 + '|' + tmp2+'"'
  cmd3 = 'ffmpeg -i {con} -c copy {to}'.format(con=conc,to=tmpout)
  cmd4 = 'ffmpeg -i {to} -qscale:v 2 {fv}'.format(to=tmpout,fv=finalVideo)
  cmd5 = 'del {t1} {t2} {to}'.format(t1=tmp1,t2=tmp2,to=tmpout)
  result = shell.runCmd(cmd1)
  result = shell.runCmd(cmd2)
  result = shell.runCmd(cmd3)
  result = shell.runCmd(cmd4)
  result = shell.runCmd(cmd5)
  print("join success!!!\n")

def get_audio(shell):
  print ("===退出程序输入exit或者bye即可 (阿玲专属程序-LG)===")
  mypathlist = os.getcwd().split('\\')#input('输入视频路径,ex: F:/cut_Video_python \n>>>').split('\\')
  if len(mypathlist)==1:
    mypath=mypathlist[0]
  else:
    mypath='/'.join(mypathlist)
  input0 = "cd "+mypath
  if input0 == 'cd exit' or input0 == 'cd bye' :
    return -1
  else :
    result = shell.runCmd(input0)

  oldvideo = input('输入视频全称,ex: oldvideo.mp4 \n>>>')  
  if oldvideo == 'exit' or oldvideo == 'bye' :
    return -1
  myaudio = input('输出音频全称,ex: myaudio.mp3 \n>>>')  
  if myaudio == 'exit' or myaudio == 'bye' :
    return -1
  input1="ffmpeg -i {ov} -f mp3 {ev}".format(ov=oldvideo,ev=myaudio)
  result = shell.runCmd(input1)
  if result[2]==None:
    print("get_audio success!!!\n")

def scale(shell):
  print ("===退出程序输入exit或者bye即可 (阿玲专属程序-LG)===")
  mypathlist = os.getcwd().split('\\')#input('输入视频路径,ex: F:/cut_Video_python \n>>>').split('\\')
  if len(mypathlist)==1:
    mypath=mypathlist[0]
  else:
    mypath='/'.join(mypathlist)
  input0 = "cd "+mypath
  if input0 == 'cd exit' or input0 == 'cd bye' :
    return -1
  else :
    result = shell.runCmd(input0)

  oldvideo = input('输入视频全称,ex: oldvideo.mp4 \n>>>')  
  if oldvideo == 'exit' or oldvideo == 'bye' :
    return -1
  set_alpha = input('下方遮挡高度(高度的1/x,整数),ex: 3 \n>>>')
  if set_alpha == 'exit' or set_alpha == 'bye' :
    return -1
  myaudio = input('输出视频全称,ex: newvideo.mp4 \n>>>')  
  if myaudio == 'exit' or myaudio == 'bye' :
    return -1
  input1="ffmpeg -i {ov} -vf crop=iw:ih*(1-{x}):0:0 {ev}".format(ov=oldvideo,x=1/int(set_alpha),ev=myaudio)
  result = shell.runCmd(input1)
  if result[2]==None:
    print("scale success!!!\n")

#ffmpeg -i 0.blv -f mp3 1.mp3
#ffmpeg -i newvideo.mp4 -vf crop=iw/3:ih:iw/3:0 mycut.mp4 [宽高xy]
if __name__ == "__main__":
    import os,sys
    print("当前文件路径:",os.getcwd())
    from os import path 
    parent_path = os.path.dirname(os.getcwd()) #取当前目录上一级目录
    print("增加的ffmpeg文件路径:",parent_path+'\\ffmpeg\\bin')
    os.environ["PATH"] = parent_path+'\\ffmpeg\\bin'+";" + os.environ["PATH"]
    shell = Shell()
    while 1 :
      inp = input(
      "CUT or JOIN or Get_Audio? \n1 for cutting video \n2 for joining two videos \n3 for geting the audio \n4 for geting bottom scale\n>>>")
      if inp == 'exit' or inp == 'bye' :
        break
      if inp == "1":
        onError=cut(shell)
        if onError==-1:
          break
      elif inp == "2":
        onError=join(shell)
        if onError==-1:
          break
      elif inp == "3":
        onError=get_audio(shell)
        if onError==-1:
          break
      elif inp == "4":
        onError=scale(shell)
        if onError==-1:
          break
      else:
        print('CUT(1) or JOIN(2) or Get_Audio(3) or Scale(4)? Select Error!!!')




      # print ("返回码：", result[0])
      # print ("标准输出：", result[1])
      # print ("标准错误：", result[2])

#ffmpeg -ss 00:00:00 -i oldvideo.mp4 -c copy -t 60 2.mp4
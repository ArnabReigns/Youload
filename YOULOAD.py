import dataclasses
import os
from platform import system
from pytube import YouTube
from pytube.cli import on_progress
from rich.jupyter import display
from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.progress import Progress
from os import name, path, sep, system
from pathlib import Path


system('mode con: cols=135')

console = Console()
progress  = Progress()

downloads_path = f"{Path.home()}\Downloads"

print("""


    .............................................................................................................................


    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░████████████████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
    █░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
    █░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█
    ███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
    ███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█
    █████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█
    ███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░████████████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░▄▀▄▀░░█
    ███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
    ███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░███
    █████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

                                    _                                    _            _           _   _            _           
                                    | |                                  | |          | |         | | | |          (_)          
                                    | |__  _   _    __ _ _ __ _ __   __ _| |__     ___| |__   __ _| |_| |_ ___ _ __ _  ___  ___ 
                                    | '_ \| | | |  / _` | '__| '_ \ / _` | '_ \   / __| '_ \ / _` | __| __/ _ \ '__| |/ _ \/ _ \ 
                                    | |_) | |_| | | (_| | |  | | | | (_| | |_) | | (__| | | | (_| | |_| ||  __/ |  | |  __/  __/
                                    |_.__/ \__, |  \__,_|_|  |_| |_|\__,_|_.__/   \___|_| |_|\__,_|\__|\__\___|_|  | |\___|\___|
                                            __/ |                                                                 _/ |          
                                            |___/                                                                 |__/            

    ..............................................................................................................................

    """)    

print("")                                                                                              
print("")


def start():   

    url = input(">> paste the url: ")


    video = YouTube(url,on_progress_callback=progressbar)

    print()
    print(">> fetching...")
    print()
    print('>> we found', colored(video.title,'red'),'by', colored(video.author,'yellow'))
    print()
    takeReq(video)

def takeReq(video):

    text = '>> press 1 for'+colored(' audio ','yellow')+'and 2 for'+colored(' video ','yellow')+': '
    quary = int(input(text))
    if quary == 1 :
        Audio(video)
    elif quary ==2:
        Video(video)
    else:
        print('>> enter 1 or 2')
        takeReq(video)   

def progressbar(stream, chunk, bytes_remaining):
    x = ((stream.filesize - bytes_remaining)/stream.filesize)*100
    print(f">> {round(x) } % completed")

def Video(video):
    table = Table(title="AVAILABLE VIDEO FORMATS TO DOWNLLOAD")

    table.add_column("INDEX", justify="center", style="white")
    table.add_column("NAME", justify="left", style="cyan")
    table.add_column("RESOLUTION", justify="center", style="green")
    table.add_column("SIZE", style="magenta", justify="right")

    print()
    print('>> getting the list......')
    print()
    list = video.streams.filter(progressive=True)
    print() 
    print(">> we have found "+colored(len(list),"red")+" files to download:")

    for idx,value in enumerate(list):

        if value.filesize < 1024:
            size = "{:.2f}".format(value.filesize/1024)
            unit = "kb"
        else:
            size = "{:.2f}".format(value.filesize/(1024*1024))
            unit = "mb"
        # print(f"{idx+1} name: {value.default_filename}, quality: {value.resolution}, download size: {size}{unit}")
        table.add_row( f">> {idx+1}",f"{value.default_filename}",f"{value.resolution}",f"{size}{unit}")

  
    print()
    console.print(table)
    print()


    fileIndex = int(input(">> enter the index of the video to download: "))

    

    def download(fileIndex):

        

        if isinstance(fileIndex,int) and (fileIndex <= len(list)) and (fileIndex >= 0):
            title = f"{list[fileIndex-1].title}"

            remove = ['\\','/',':','*','?','"','<','>','|']
            
            for f in remove:
                title = title.replace(f," ")
            dest= Path(f"{downloads_path}\{title}.{list[fileIndex-1].subtype}")
            i = 0 
            p = title
            while dest.is_file():
                i = i+1
                p = f"{title}({i})"
                dest =  Path(f"{downloads_path}\{p}.{list[fileIndex-1].subtype}")
            
            title = p
            
            

            print()
            print(">>  downloaing....")
            print()
            list[fileIndex-1].download(output_path=downloads_path,filename = f"{title}.{list[fileIndex-1].subtype}")
            print()
            print(f">> file location : {dest}")
            print()
            print()
            print("..................................................................................................................................")
            print()
            print()
        else:
            print()
            print(f">> maximum index => {len(list)}")
            print(f">> minimum index => 1")
            print()
            print(colored(f'>> you entered => {fileIndex}     :) ','red'))
            print()
            retry = int(input(">> enter the index properly: "))
            download(retry)
    
    download(fileIndex)

def Audio(Video):

    table = Table(title="AVAILABLE AUDIO FORMATS TO DOWNLLOAD")

    table.add_column("INDEX", justify="center", style="white")
    table.add_column("NAME", justify="left", style="cyan")
    table.add_column("QUALITY", justify="center", style="green")
    table.add_column("SIZE", style="magenta", justify="right")
    
    print()
    print('>> getting the list......')
    print()
    list = Video.streams.filter(only_audio=True )
    print() 
    print(">> we have found "+colored(len(list),"red")+" files to download:")

    for idx,value in enumerate(list):
    
        if value.filesize/1024 < 1024:
            size = "{:.2f}".format(value.filesize/1024)
            unit = "kb"
        else:
            size = "{:.2f}".format(value.filesize/(1024*1024))
            unit = "mb"

        if value.bitrate/1024 < 1024:
            quality = round(value.bitrate/1024)
            qunit = "kbps"
        elif value.bitrate/1024 > 1024:
            quality = round(value.bitrate/(1024*1024))
            qunit = "mbps"

        # print(f"{idx+1} name: {value.default_filename}, quality: {value.resolution}, download size: {size}{unit}")
        table.add_row( f">> {idx+1}",f"{value.title}.mp3",f"{quality}{qunit}",f"{size}{unit}")

    print()
    console.print(table)
    print()
    fileIndex = int(input(">> enter the index of the Audio to download: "))

    def download(fileIndex):

        
        print()
        if isinstance(fileIndex,int) and fileIndex <= len(list) and fileIndex > 0:
            title = f"{list[fileIndex-1].title}"
            

            remove = ['\\','/',':','*','?','"','<','>','|']
            
            for f in remove:
                title = title.replace(f," ")
            dest= Path(f"{downloads_path}\{title}.mp3")
            i = 0 
            a = title


            while dest.is_file():
                i = i+1
                a = f"{title}({i})"
                dest =  Path(f"{downloads_path}\{a}.mp3")
                
            
            title = a


            print()
            print(">>  downloaing....")
            print()
            file=list[fileIndex-1].download(output_path=downloads_path,filename=f"{title}.mp3")
            print()
            print(colored(f">> file location : {dest}","green"))
            print()
            print()
            print("..................................................................................................................................")
            print()
            print()
        else:
            print()
            print(f">> maximum index => {len(list)}")
            print(f">> minimum index => 1")
            print()
            print(colored(f'>> you entered => {fileIndex}     :) ','red'))
            print()
            retry = int(input(">> enter the index properly: "))
            download(retry)
    
    download(fileIndex)

while True:
    try:
        start()
    except:
        print()
        print(colored('you might have entered an incorrect url. Please try again','red'))
        print()



# believer song link:      https://www.youtube.com/watch?v=7wtfhZwyrcc
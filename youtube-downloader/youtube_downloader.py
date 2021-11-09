
from pytube import YouTube
from tkinter import *
from tkinter.filedialog import *
from threading import *

font = ('verdana', 20)
file_size = 0

# on complete callback function
def complete_download(stream=None, file_path=None):
    download_btn['text'] = 'Download Video'
    download_btn['state'] = 'active'
    url_field.delete(0, END)
    print('Download completed!')

# on progress callback function
def progress_download(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    download_btn['text'] = '{:00.0f}% downloaded '.format(percent)

# download function
def start_download(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.get_highest_resolution()

        yt.register_on_complete_callback(complete_download)
        yt.register_on_progress_callback(progress_download)

        file_size = st.filesize
        st.download(output_path=path_to_save)

    except Exception as e:
        print(e)
        print('something whent wrong')

def btn_clicked():
    try:
        download_btn['text'] = 'Please wait...'
        download_btn['state'] = 'disabled'
        url = url_field.get()
        if url == '':
            download_btn['text'] = 'Download Video'
            download_btn['state'] = 'active'
            return

        print(url)
        thread = Thread(target=start_download, args=(url,))
        thread.start()
    
    except Exception as e:
        print(e)

# GUI

root = Tk()
root.title('YouTube Downloader')
root.iconbitmap('img/youtube_icon-icons.com_72036.ico')
root.geometry('500x250')

# main icon section
file = PhotoImage(file='img/1441800209_youtube_47117.png')
heading_icon = Label(root, image=file)
heading_icon.pack(side=TOP, pady=3)
# making url field
url_field = Entry(root, font=font, justify=CENTER)
url_field.pack(side=TOP, fill=X, padx=10)
url_field.focus()

# download btn
download_btn = Button(root, text='Download Video', font=font, relief='ridge', command=btn_clicked) 
download_btn.pack(side=TOP, pady=20)

root.mainloop()
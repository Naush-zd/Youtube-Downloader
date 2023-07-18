import tkinter
import customtkinter
from pytube import YouTube
import threading


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = (bytes_downloaded / total_size) * 100
    per = str(int(percentage_of_completion)) + "%"
    percentage.configure(text=per, text_color="white")
    percentage.update()
    progress.set(float(percentage_of_completion)/100)


def startdownload():
    try:
        url = url_var.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        label.configure(text=yt.title)
        finishlabel.configure(text="")
        thread = threading.Thread(
            target=yt.streams.get_highest_resolution().download())
        thread.start()
        thread.join()
        finishlabel.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        print(e)
        finishlabel.configure(text="Error!", text_color="red")


# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# Create window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")


# Create widgets
label = customtkinter.CTkLabel(
    app, text="YouTube Downloader", font=("Arial", 20))
label.pack(pady=20)

# url entry
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, textvariable=url_var)
link.pack()

# download button
download = customtkinter.CTkButton(
    app, text="Download", width=20, command=startdownload)
download.pack(pady=20)

# progress percentage
percentage = customtkinter.CTkLabel(app, text="", font=("Arial", 20))
percentage.pack()

# progress bar
progress = customtkinter.CTkProgressBar(app, width=400)
progress.set(0)
progress.pack()


# finish label
finishlabel = customtkinter.CTkLabel(app, text="", font=("Arial", 20))
finishlabel.pack(pady=20)

# run the app
app.mainloop()

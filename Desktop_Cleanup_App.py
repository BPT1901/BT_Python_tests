import customtkinter
import os
import shutil
import time

import send2trash
from datetime import datetime

#Creating the variables for the program to reference
desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
cleanup_folder = 'Cleanup'
cleanup_dir = os.path.join(desktop_dir, cleanup_folder)
screen_dir = 'Screenshots'
images_dir = 'Images'
movies_dir = 'Videos'
audio_dir = 'Audio'
others_dir = 'Others'
path1 = os.path.join(cleanup_dir, screen_dir)
path2 = os.path.join(cleanup_dir, images_dir)
path3 = os.path.join(cleanup_dir, movies_dir)
path4 = os.path.join(cleanup_dir, audio_dir)
path5 = os.path.join(cleanup_dir, others_dir)
now = datetime.now()
current_time = now.strftime('%H:%M:%S')


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()

root.title('Desktop Cleanup')
root.geometry('450x160')
root.grid_columnconfigure(0, weight=1)

#def get_progress():
    #for i in range(1, 101):
        #print(f'{i}%', end='\r')
        #time.sleep(0.015)
    #get_progress
    
#Main Function for the cleanup
def cleanup():
    os.makedirs(cleanup_dir)
    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)
    os.makedirs(path4)
    os.makedirs(path5)
    #print('Creating Cleanup Folder...')

     #Loop through all files on desktop   
    imgs = ('pdf', 'jpg', 'HEIC', 'jpeg', 'png')
    movies = ('mp4', 'mov', 'MOV')
    others = ('zip', 'dmg', 'xls', 'xml', 'webp')
    audio = ('mp3, wav, aac')
    files_on_desktop = os.listdir(desktop_dir)
     # if there is a screenshot move it to screenshots folder
    for file in files_on_desktop:
        if file.startswith('Screenshot') or file.startswith('Screen Shot'):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path1)
            print(f'Moving {file}')
    #if there is an image, move it to the images folder
        elif file.endswith(imgs):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path2)
            print(f'Moving {file}')
    # if there is a video, move to videos folder
        elif file.endswith(movies):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path3)
            print(f'Moving {file}')
        elif file.endswith(audio):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path4)
            print(f'Moving {file}')
        elif file.endswith(others):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path5)
            print(f'Moving {file}')
            time.sleep(.05)
            label.configure(text=f'Cleanup folder completed at: {current_time}', text_color='DeepSkyBlue2')
            
#print(f'Cleanup folder completed at: {current_time}')      
    
def update_progress_label(progress_label):
    for i in range(1, 101):
        progress_label.configure(text=f'Progress: {i}%', text_color='DeepSkyBlue2')
        progress_label.update()
        time.sleep(0.010)   

#def cont_button_func():
    #print('This worked')
    #time.sleep(.05)
    #label.configure(text=f'Cleanup folder completed at: {current_time}', text_color='DeepSkyBlue2')
    
def later_button_func():
    print('Working')
    
label = customtkinter.CTkLabel(root, text='Would you like to create a cleanup folder for all desktop files?')
label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

progress_label = customtkinter.CTkLabel(root, text='')
progress_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
#update_progress_label(progress_label)

cont_button = customtkinter.CTkButton(root, text='Continue', text_color='Black', command=lambda: [update_progress_label(progress_label), cleanup()], fg_color='DeepSkyBlue2')
cont_button.grid(row=2, column =0, padx=10, pady=10, sticky='w')

later_button = customtkinter.CTkButton(root, text='Later', text_color='Black', command=later_button_func, fg_color='DeepSkyBlue2')
later_button.grid(row=2, column =1, padx=10, pady=10, sticky='e')

root.mainloop()




#lambda: [progress(), cont_button_func()] 
import tkinter
import tkinter.filedialog
from PIL import Image, ImageTk
import os


root = tkinter.Tk()
root.title = 'new'
root.geometry('820x520')
root.resizable(0,0)#禁止窗口大小调整
label1 = tkinter.Label(root,text='源图片')
label1.place(x=200,y=10)
label1 = tkinter.Label(root,text='处理后图片')
label1.place(x=570,y=10)
#图片框大小
w_box = 400
h_box = 400


def dosth_func():
    pth = inputDir.replace("/",'\\')
    os.system("copy %s D:\originpic" % (pth))
    os.system("python test.py --dataroot d:\originpic --model test --learn_residual")

    #在此调用你的函数，输入图片的路径是inputDir，处理后生成的图片路径输出到outDir中

    outDir=inputDir #这个路径应该由你的程序运行后得到，这里直接用input展示效果
    print('处理后图片:',outDir)
    showImg(outDir)


def resize(w, h, w_box, h_box, loadimage):  
    f1 = 1.0*w_box/w
    f2 = 1.0*h_box/h  
    factor = min([f1, f2])  
    width = int(w*factor)  
    height = int(h*factor)  
    return loadimage.resize((width, height), Image.ANTIALIAS)


inputDir = ''
def choose_fiel():
    global inputDir
    try:
        inputDir = tkinter.filedialog.askopenfilename(title='选择文件')  # 选择文件
        print('源图片:',inputDir)
        load = Image.open(inputDir)
        w, h = load.size
        load_resized = resize(w, h, w_box, h_box, load)
        render = ImageTk.PhotoImage(load_resized)
        img = tkinter.Label(root,imag=render,width=w_box,height=w_box)
        img.image = render
        img.place(x=10,y=50)
    except:
        pass


def showImg(outDir):
    load = Image.open(outDir)
    w, h = load.size
    load_resized = resize(w, h, w_box, h_box, load)
    render = ImageTk.PhotoImage(load_resized)
    img = tkinter.Label(root,imag=render,width=w_box,height=w_box)
    img.image = render
    img.place(x=410,y=50)



submit_button = tkinter.Button(root, text ="处理", command = dosth_func)
submit_button.pack(side='bottom')
submit_button = tkinter.Button(root, text ="选择图片", command = choose_fiel)
submit_button.pack(side='bottom')

root.mainloop()

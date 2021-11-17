from tkinter import * #GUI 라이브러리 
import tkinter #GUI 라이브러리
import hashlib #해쉬 라이브러리
import clipboard #복사 기능 라이브러리
import webbrowser #웹 브라우저 실행 라이브러리

encryption_text = ''
none_text = ''


#------------------------------------------------

#tkinter 기본 설정

root = Tk()
root.title("Hash Encryption Program")
root.geometry("700x400+450+150")
root.resizable(False, False)

#-------------------------------------------------

#기능 함수(해쉬 생성 및 기타 기능) 코드


def close():
    root.destroy()

def md5(): #md5 해쉬 생성
    md5_hash = hashlib.md5()
    none_text = txt.get("1.0", END)
    none_text = none_text.encode('utf-8')
    md5_hash.update(none_text)
    encryption_text = md5_hash.hexdigest()
    labelconfig(encryption_text)
    copy(encryption_text)

def sha1(): #sha1 해쉬 생성
    sha1_hash = hashlib.sha1()
    none_text = txt.get("1.0", END)
    none_text = none_text.encode('utf-8')
    sha1_hash.update(none_text)
    encryption_text = sha1_hash.hexdigest()
    labelconfig(encryption_text)
    copy(encryption_text)

def sha256(): #sha256 해쉬 생성
    sha256_hash = hashlib.sha256()
    none_text = txt.get("1.0", END)
    none_text = none_text.encode('utf-8')
    sha256_hash.update(none_text)
    encryption_text = sha256_hash.hexdigest()
    labelconfig(encryption_text)
    copy(encryption_text)

def sha512(): #sha512 해쉬 생성
    sha512_hash = hashlib.sha512()
    none_text = txt.get("1.0", END)
    none_text = none_text.encode('utf-8')
    sha512_hash.update(none_text)
    encryption_text = sha512_hash.hexdigest()
    labelconfig(encryption_text)
    copy(encryption_text)

def reset(): #결과 값 리셋
    labelconfig('None')

def copy(encryption_text):
    clipboard.copy(encryption_text)

def github():
    url = 'https://github.com/incheon43/HasH-Encryption-Program'
    webbrowser.open(url)

def blog():
    url = 'https://ye0ngjae.tistory.com/'
    webbrowser.open(url)

#-------------------------------------------------

#메뉴바 구성 코드

menubar = tkinter.Menu(root)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label='blog', command=blog)
menu_1.add_command(label='github', command= github)
menu_1.add_separator()
menu_1.add_command(label='EXIT', command=close)
menubar.add_cascade(label='HELP', menu=menu_1)
root.config(menu=menubar)

#-------------------------------------------------

#주 화면 구성 코드

txt = Text(root, width=40, height=1)
txt.place(x=100, y=120)

btn1 = Button(root, width=13, height=2, text="MD5", command=md5)
btn1.place(x= 550, y= 100)

btn3 = Button(root, width=13, height=2, text="SHA-1", command=sha1)
btn3.place(x= 550, y= 160)

btn4 = Button(root, width=13, height=2, text="SHA-256", command=sha256)
btn4.place(x= 550, y= 220)

btn5 = Button(root, width=13, height=2, text="SHA-512", command=sha512)
btn5.place(x= 550, y= 280)

btn2 = Button(root, width=20, height=1, text='Reset', command=reset)
btn2.place(x=160, y=310)

label1 = Label(root, text='Hash Encryption Program', font=('나눔고딕', 30))
label1.place(x=10, y=10)

label2 = Label(root, text='Enter unencrypted string')
label2.place(x=100,y=90)

label3 = Label(root, text='Encryption string')
label3.place(x=100,y=250)

label4 = Label(root, text='None', width=40, height=1, bg='white')
label4.place(x=100,y=280)

def labelconfig(encryption_text):
    label4.config(text=encryption_text)

root.mainloop() #프로그램 실행

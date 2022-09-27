import random
mon=random.randint(1,3)

def syutudai():
    if mon==1:
        print("人気漫画ONEPIECEに出てくる「ひとつなぎの大秘宝ワンピース」の正体は？")
    elif mon==2:
        print("1+1=?")
    else:
        print("5-1=?")

def kaitou():
    x=input("回答：")
    if mon==1:
        print("不正解")
    elif mon==2:
        if x=="2":
            print("正解")
        else:
            print("不正解")
    else:
        if x=="4":
            print("正解")
        else:
            print("不正解")
    
if __name__ == "__main__":
    syutudai()
    kaitou()
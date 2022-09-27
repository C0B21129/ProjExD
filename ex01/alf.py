import random
kesu=random.randint(0,5)
moji=["A","R","D","S","L","F"]
def toi():
    print(moji)
    nuki=moji.pop(kesu)
    print(moji)
    tou=input()
    if tou==nuki:
        print("正解")
    else:
        print
        ("不正解")
        toi()
        
    
if __name__ == "__main__":
    toi()
    
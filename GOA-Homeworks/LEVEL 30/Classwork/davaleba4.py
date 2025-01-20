# საკლასო დავალება:
# შექმენით ფუნქცია სახელად manual_swapcase

def manual_swapcase(main_str):
    res = ""

    for char in range(len(main_str)):
        if char.islower(): res += char.upper()
        else: res += char.lower()

        print(res)

manual_swapcase = ("wd sawd saw dsawd sa w d,aw dsaw ")
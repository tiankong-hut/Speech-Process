# coding=utf-8
# 被shiyan_1.py调用
def func():
    print("func() in shiyan_1.py")
    print ("Path: /Neural network/shiyan_3")
print("top-level in one.py")

if __name__ == "__main__":
    print("shiyan_3.py is being run directly")
else:
    print("shiyan_3.py is being imported into another module")


import time

def jack_wake_up():
    ##
    # TODO: Jack 請把 for loop 的註解取消
    ##
    for x in range(3):
        time.sleep(1)
        print("Z...", end=" ")

    print("Jack: Okok..., I'm going to get up :(")

if __name__ == '__main__':
    print("Jack: Hey, My name is Jack ;)")

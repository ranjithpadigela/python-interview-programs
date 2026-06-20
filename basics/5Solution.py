# Find the missing number in squence.

def missing_sequence(L,start,end,missing_num):
    full_list = range(start,end+1)
    count = 0
    inp_index = 0
    for item in full_list:
        if item != L[inp_index]:
            print(item)
            count += 1
        else:
            inp_index += 1
        if count > missing_num:
            break


def main():
    L = [10,11,13,14,15,16,17,18,20]
    start = 10
    end = 20
    missing_sequence(L,start,end,2)



if __name__ == "__main__":
    main()  
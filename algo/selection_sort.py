data = [10, 20, 80, 15, 18, 98, 75, 44, 77]

def selectionSort(list_data):

    # mengecek array data dari index paling belakang
    for index in range(len(list_data) - 1, 0, -1):
        biggest_data = 0

        # mencari data terbesar dalam array data. -1 tiap iterasi
        for data in range(1, index + 1):
            if list_data[data] > list_data[biggest_data]:
                biggest_data = data

        # menukar index array data agar tersortir.
        temp = list_data[index]
        list_data[index] = list_data[biggest_data]
        list_data[biggest_data] = temp

def main():
    print(f"unsorted list: {data}")
    selectionSort(data)
    print(f"sorted list: {data}")

if __name__ == "__main__":
    main()
step_counter = 1

def merge_sort(arr):
    global step_counter
    # Split
    # Recursion - Keep splitting into left and right halves until array length is 1 (which is not greater than 1)
    if len(arr) > 1: # stop condition for recursion
        mid = len(arr) // 2 # rounds down to nearest whole number
        left_half = arr[:mid] # numbers from start of array up to, but not including mid
        right_half = arr[mid:] # numbers from mid to end of array

        # recursion
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge
        l = r = a = 0 # 3 "pointers" to track current position. l is for tracking left half, r for right half, and a for the array.

        while l < len(left_half) and r < len(right_half): # iterates while there are still numbers left
            if left_half[l] < right_half[r]: # Compare left element to right element
                arr[a] = left_half[l] # Put into array if less (since sorting from lowest to highest)
                l += 1 # increase pointer
            else:
                arr[a] = right_half[r] # Put into array if less
                r += 1 # increase pointer
            a += 1 # increase array pointer everytime since one is element is added each time

        # Adds remaining elements left over in the left half (when one half has more elements than the other or when the elements in one half are smaller than the other)
        while l < len(left_half):
            arr[a] = left_half[l]
            l += 1
            a += 1

        # Adds remaining elements left over in the right half (when one half has more elements than the other or when the elements in one half are smaller than the other)
        while r < len(right_half):
            arr[a] = right_half[r]
            r += 1
            a += 1

        print(f'Step {step_counter}: {arr}')
        step_counter += 1

def main():
    arr = list(map(int, input("Enter numbers separated by spaces: ").split())) # Splits the numbers based on empty space, then uses map to apply int function on each number, 
                                                                               # then converts the map iterator to a list
    print("Initial array:", arr)
    merge_sort(arr)
    print("Merge Sorted array:", arr)

if __name__ == "__main__":
    main()
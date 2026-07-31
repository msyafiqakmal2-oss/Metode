This Is Not On Purpose
And Not Very Fine

But In The Next Time I Can be Improve From This Maybee You Can see just a few words but in the next time   

<li> Function Definition: bubbleSort </li>

The function bubbleSort(arr) takes a list of integers as an input and returns the sorted list.

    Outer Loop: It iterates through the entire list to ensure every element is checked.

    Inner Loop: It compares adjacent elements. The range is shortened by index each time because, after every pass, the largest remaining element "bubbles up" to its correct position at the end of the list.

    Swapping: If the current element (arr[inner_index]) is greater than the next one (arr[inner_index + 1]), their positions are swapped.

<li> Data Generation </li>

    The variable n = 100 defines the number of elements.

    A list named data is initialized.

    A for loop populates the list with 100 random integers, each ranging between 1 and 1000, using the random.randint method.

<li> Execution and Performance Measurement </li>

    Start Time: now = time.time() captures the exact timestamp before the sorting begins.

    Sorting: The bubbleSort(data) function is called and the sorted result is printed.

    End Time: then = time.time() captures the timestamp immediately after the function completes.

    Calculation: The script calculates total_time by subtracting the start time from the end time.

<li> Output </li>

Finally, the script prints:

    The original unsorted random list.

    The final sorted list.

    The total time taken for the sorting process in seconds.

Summary of Complexity

  =  Algorithm: Bubble Sort.
Time Complexity: O(n2), which means the time taken increases exponentially as the list size grows.
Use Case: This code is typically used for educational purposes to understand how sorting works, rather than for production environments where faster algorithms like QuickSort or Python's built-in .sort() (Timsort) are preferred.

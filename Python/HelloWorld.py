from array import array

def sequential_search(arr, search):
    for i in range(len(arr)-1):
        if arr[i] == search:
            return i
    return -1

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
def printArray(arr):
    print("\n")  
    for i in range(len(arr)):
        print(arr[i], " ", end='')
    print("\n")
        
        
int_array = array('i', [5, 4, 3, 2, 1])
size = len(int_array)
found = sequential_search(int_array, 5)
print(found)
print(size)
printArray(int_array)
bubbleSort(int_array)
printArray(int_array)

'''
/**
	 * bubblesortArray method sorts a String array 
	 * in alphanumeric order
	 * @param array
	 */
	public static void bubbleSort(String[] array)
    {
		// Print array before sort
		System.out.println("Before Sort: ");
        toString(array);
        System.out.println();
        
		for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j].compareToIgnoreCase(array[j + 1]) > 0) {
                    String temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
		
		// Print array after sort
		System.out.println("After Sort: ");
        toString(array);
        System.out.println();
    }
'''   
'''
public static int sequentialSearch(int[] array, int search) {
		
		
		for ( int i = 0; i < array.length; i++ ) {
			if ( array[i] == search) {
				return i;
			}
		}
		return -1;
	}
'''



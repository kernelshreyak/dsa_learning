/*
Arrange the array in following form: [min,max,2nd min,2nd max,......]
*/
package main

import (
	"fmt"
	"sort"
)

func main() {
	var arr = []int{1, 6, 100, 200, 300, 500, 2, -1, 8} // okay
	var arr2 = []int{}

	sort.Ints(arr)
	var j = len(arr) - 1 //back pointer
	for i := range arr { // front pointer

		// append min
		arr2 = append(arr2, arr[i])

		if i > j || arr[i] == arr[j] {
			break
		}

		// append max
		arr2 = append(arr2, arr[j])
		j -= 1

	}
	fmt.Println(arr)
	fmt.Println(arr2)
}

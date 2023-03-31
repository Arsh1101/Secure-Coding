package main

import "fmt"

//Slice can over expand
//And there is no rules to check the length
func wrongCode(length int) {
	var slice []int
	for i := 0; i < length; i++ {
		slice = append(slice, i)
	}
	fmt.Println(slice)
}

func correctCode(length int) {
	//Check validations
	if length > 13 || length < 0 {
		return
	}
	slice := make([]int, 0, length) // pre-allocate the slice with a capacity in a range
	for i := 0; i < length; i++ {
		slice = append(slice, i)
	}
	fmt.Println(slice)
}

func main() {
	wrongCode(100)
	correctCode(10)
}

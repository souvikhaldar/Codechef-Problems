package main

import (
	"fmt"
)

func main() {
	var T, N int
	var S string
	fmt.Scanf("%d", &T)
	for j := 0; j < T; j++ {
		fmt.Scanf("%d", &N)
		fmt.Scanf("%s", &S)
		if N%2 == 0 {
			U := []rune(S)
			for i := 0; i < N; i += 2 {
				temp := U[i]
				U[i] = U[i+1]
				U[i+1] = temp
			}
			for i := 0; i < len(S); i++ {
				U[i] = rune(int('z') - int(U[i]) + 97)
			}
			fmt.Println(string(U))
		} else {
			U := []rune(S)
			for i := 0; i < N-1; i += 2 {
				temp := U[i]
				U[i] = U[i+1]
				U[i+1] = temp
			}
			for i := 0; i < len(S); i++ {
				U[i] = rune(int('z') - int(U[i]) + 97)
			}
			fmt.Println(string(U))
		}

	}
}

package main

import "fmt"

func check(a []int, b []int) bool {
	for _, aValue := range a {
		flag := 0
		for _, bValue := range b {

			if aValue == bValue {
				flag = 1
			}
		}
		if flag == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int

	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		var Tr, Dr, Ts, Ds int
		var TrS, DrS, TsS, DsS []int
		fmt.Scanf("%d", &Tr)
		for j := 0; j < Tr; j++ {
			var value int
			fmt.Scanf("%d", &value)
			TrS = append(TrS, value)
		}
		fmt.Scanf("%d", &Dr)
		for j := 0; j < Dr; j++ {
			var value int
			fmt.Scanf("%d", &value)
			DrS = append(DrS, value)
		}
		fmt.Scanf("%d", &Ts)
		for j := 0; j < Ts; j++ {
			var value int
			fmt.Scanf("%d", &value)
			TsS = append(TsS, value)
		}
		fmt.Scanf("%d", &Ds)
		for j := 0; j < Ds; j++ {
			var value int
			fmt.Scanf("%d", &value)
			DsS = append(DsS, value)
		}
		a := check(TsS, TrS)
		b := check(DsS, DrS)
		if a == true && b == true {
			fmt.Println("yes")
		} else {
			fmt.Println("no")
		}
	}

}

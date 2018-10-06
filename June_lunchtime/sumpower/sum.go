package main

import (
	"fmt"
	"log"
)

func main() {
	var a string
	var b int
	_, e := fmt.Scanf("%d", &b)
	if e != nil {
		log.Panic()
	}
	for i := b; i > 0; i-- {
		var n, k int
		fmt.Scanf("%d %d", &n, &k)
		c := make([]string, (n - k + 1))

		fmt.Scanf("%s", &a)

		for b := 0; b < (n - k + 1); b++ {
			c[b] = a[b:(b + k)]
		}
		count := 0
		for l := 1; l < len(c); l++ {
			for m := 0; m < k; m++ {
				count = count + int(c[l][m]-c[l-1][m])
			}
		}
		fmt.Println(count)

	}
}

package main

import (
	"fmt"
	"log"
)

func main() {
	var i, j, k int
	_, er := fmt.Scanf("%d", &k)
	if er != nil {
		log.Panic()
	}
	for l := k; l > 0; l-- {
		count := 0
		_, e := fmt.Scanf("%d %d", &i, &j)
		if e != nil {
			log.Panic()
		}
		for a := i; a <= j; a++ {
			b := a % 10
			if b == 2 || b == 3 || b == 9 {
				count++
			}
		}
		fmt.Println(count)
	}

}

package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()

	// 执行一些耗时的操作，例如计算斐波那契数列的第40个数
	result := fibonacci(40)

	elapsed := time.Since(start)

	fmt.Printf("Fibonacci(40) = %d\n", result)
	fmt.Printf("Time taken: %s\n", elapsed)
}

func fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

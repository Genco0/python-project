# Assignment-009/5 (Fibonacci Numbers)
fibonacci_nb = [1, 1]
count = 0
while fibonacci_nb[count] < 34 :
  fibonacci_nb.append(fibonacci_nb[count]+fibonacci_nb[count+1])
  count += 1
fibonacci_nb

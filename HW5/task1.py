multiplication_table = (f"{i}x{j}={i*j}" for i in range(2, 10) for j in range(2, 11))

print(*multiplication_table, sep='  ')

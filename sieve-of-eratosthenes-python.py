def sieve_of_eratosthene(N):

    # Cria-se uma lista referente a todos os inteiros entre 0 e N:
    A = [True] * (N+1)

    # Define os números 0 e 1 como não primos:
    A[0] = A[1] = False

    # Percorra a lista até encontrar o primeiro número primo:
    for value, prime in enumerate(A):

        # O número é primo?
        if prime:

            # Retorna o número primo:
            yield value

            # Remova da lista todos os múltiplos do número enontrado:
            for i in range(value**2, N+1, value):
                A[i] = False

primes = list(sieve_of_eratosthene(100))

print(primes) 

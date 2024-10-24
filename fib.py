def fibseq(N):
    v = [0, 1]  # Initial list containing the first two Fibonacci numbers: 0 and 1
    for i in range(N):  # Loop N times to generate the sequence
        v.append(sum(v[-2:]))  # Append the sum of the last two elements of v to extend the sequence
        print(v)  # Print the updated sequence at each step

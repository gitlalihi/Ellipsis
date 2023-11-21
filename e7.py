#Python program to create a generator expression that generates a sequence of numbers with ellipsis representing skipped values.
def generate_sequence(start, end, step, skip):
    return (i if i % skip == 0 else '...' for i in range(start, end, step))


sequence_with_ellipsis = generate_sequence(1, 20, 2, 3)
for value in sequence_with_ellipsis:
    print(value, end=' ')
import random


DNA_BASES = ["A", "C", "G", "T"]


def generate_reference(length=200):
    return "".join(
        random.choice(DNA_BASES)
        for _ in range(length)
    )


def introduce_variant(sequence, position, new_base):
    sequence = list(sequence)
    sequence[position] = new_base
    return "".join(sequence)


def simulate_read(sequence, read_length=50, error_rate=0.01):
    start = random.randint(
        0,
        len(sequence) - read_length
    )

    read = list(
        sequence[start:start + read_length]
    )

    for i in range(len(read)):
        if random.random() < error_rate:
            read[i] = random.choice(DNA_BASES)

    quality = "I" * read_length

    return "".join(read), quality


def simulate_fastq(sequence, num_reads=20, read_length=50, error_rate=0.01):
    records = []

    for i in range(num_reads):
        read, quality = simulate_read(
            sequence,
            read_length,
            error_rate
        )

        records.append(
            f"@read_{i}\n{read}\n+\n{quality}"
        )

    return "\n".join(records)


if __name__ == "__main__":
    reference = generate_reference(length=200)

    variant_position = 100
    variant_base = random.choice(DNA_BASES)

    variant_sequence = introduce_variant(
        reference,
        variant_position,
        variant_base
    )

    fastq = simulate_fastq(
        variant_sequence,
        num_reads=10,
        read_length=50,
        error_rate=0.01
    )

    print(fastq)
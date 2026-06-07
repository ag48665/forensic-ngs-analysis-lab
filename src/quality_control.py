from fastq_simulator import (
    generate_reference,
    simulate_fastq
)


def mean_quality(fastq_text):

    lines = fastq_text.split("\n")

    quality_lines = lines[3::4]

    total = 0
    count = 0

    for quality in quality_lines:
        for char in quality:
            total += ord(char) - 33
            count += 1

    return total / count


if __name__ == "__main__":

    reference = generate_reference()

    fastq = simulate_fastq(
        reference,
        num_reads=100
    )

    print(
        "Average Phred quality:",
        round(mean_quality(fastq), 2)
    )
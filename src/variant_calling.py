from collections import Counter

from fastq_simulator import (
    generate_reference,
    introduce_variant,
    simulate_fastq
)


def parse_fastq_sequences(fastq_text):
    lines = fastq_text.split("\n")
    return lines[1::4]


def call_variants(reference, reads):
    variant_counts = {}

    for read in reads:
        for i, base in enumerate(read):
            ref_base = reference[i]

            if base != ref_base:
                key = (i, ref_base, base)

                if key not in variant_counts:
                    variant_counts[key] = 0

                variant_counts[key] += 1

    return variant_counts


if __name__ == "__main__":
    reference = generate_reference(length=50)

    variant_position = 20
    variant_base = "T"

    altered_reference = introduce_variant(
        reference,
        variant_position,
        variant_base
    )

    fastq = simulate_fastq(
        altered_reference,
        num_reads=100,
        read_length=50,
        error_rate=0.01
    )

    reads = parse_fastq_sequences(fastq)

    variants = call_variants(reference, reads)

    print("Detected variants:")

    for variant, count in variants.items():
        print(variant, "count=", count)
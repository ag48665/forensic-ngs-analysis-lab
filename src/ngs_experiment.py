import pandas as pd

from fastq_simulator import (
    generate_reference,
    introduce_variant,
    simulate_fastq
)

from variant_calling import (
    parse_fastq_sequences,
    call_variants
)


results = []

for _ in range(100):

    reference = generate_reference(length=50)

    altered = introduce_variant(
        reference,
        20,
        "T"
    )

    fastq = simulate_fastq(
        altered,
        num_reads=100,
        read_length=50,
        error_rate=0.01
    )

    reads = parse_fastq_sequences(fastq)

    variants = call_variants(
        reference,
        reads
    )

    true_variant_support = 0

    for variant, count in variants.items():

        if variant[0] == 20:
            true_variant_support += count

    results.append(
        true_variant_support
    )

df = pd.DataFrame({
    "variant_support": results
})

print(
    "Average variant support:",
    df["variant_support"].mean()
)

df.to_csv(
    "reports/ngs_results.csv",
    index=False
)
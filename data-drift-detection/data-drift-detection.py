def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    reftotal = sum(reference_counts)
    prototal = sum(production_counts)

    refprob = []
    prodprob = []
    for i in reference_counts:
        refprob.append(i/reftotal)
    for i in production_counts:
        prodprob.append(i/prototal)

    tvd = 0.5 * sum(abs(r-p) for r,p in zip(refprob, prodprob))
    drift_detected = tvd > threshold
    return {'score':tvd, 'drift_detected': drift_detected}
def alphabet(w):
    w=w.lower()
    const=1
    for _ in w:
        const=const*(ord(_)-96)

    return const


print(alphabet("COMETQ")%47)
print(alphabet("HVNGAT")%47)
# Assuming your PortStemmer class is defined in port_stemmer.py
from port_stemmer import PortStemmer


def test_porter_stemmer():
    # Initialize the stemmer
    stemmer = PortStemmer()

    # Test cases: A list of words to be stemmed
    test_words = [
        "caresses",
        "flies",
        "dies",
        "mules",
        "denied",
        "died",
        "agreed",
        "owned",
        "humbled",
        "sized",
        "meeting",
        "stating",
        "siezing",
        "itemization",
        "sensational",
        "traditional",
        "reference",
        "colonizer",
        "plotted",
    ]

    # Expected results based on the Porter Stemmer algorithm
    expected_results = [
        "caress",
        "fli",
        "die",
        "mule",
        "deni",
        "die",
        "agre",
        "own",
        "humbl",
        "size",
        "meet",
        "state",
        "siez",
        "itemize",
        "sensat",
        "tradit",
        "refer",
        "colonize",
        "plot",
    ]

    # Print header for results
    print("{0:20}{1:20}{2:20}".format("Word", "Stemmed Word", "Expected Word"))

    # Iterate over each word and compare with expected result
    for word, expected in zip(test_words, expected_results):
        stemmed_word = stemmer.stem(word)
        print("{0:20}{1:20}{2:20}".format(word, stemmed_word, expected))


# Run the test function
if __name__ == "__main__":
    test_porter_stemmer()

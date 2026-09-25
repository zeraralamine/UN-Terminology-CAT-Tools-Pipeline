import csv
import rdflib

def extract_bilingual_terms(ttl_path, output_csv, src_lang="fr", tgt_lang="ar"):
    print(f"Loading UN database from {ttl_path}...")
    g = rdflib.Graph()
    g.parse(ttl_path, format="ttl")

    query = f"""
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        SELECT DISTINCT ?src ?tgt
        WHERE {{
            ?concept skos:prefLabel ?src .
            FILTER(lang(?src) = "{src_lang}")
            ?concept skos:prefLabel ?tgt .
            FILTER(lang(?tgt) = "{tgt_lang}")
        }}
    """

    print(f"Extracting {src_lang}-{tgt_lang} pairs...")
    results = g.query(query)

    print("Saving clean file...")
    with open(output_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["fr-CH", "ar-SA"])
        for row in results:
            writer.writerow([row.src, row.tgt])
    print("Done!")

if __name__ == "__main__":
    extract_bilingual_terms("unbis-thesaurus.ttl", "UN_French_Arabic_Clean.csv")

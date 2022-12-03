def parse_gene_paths(table_text: str) -> dict:
    gene_in_path = {}
    rows = table_text.split("\n")
    for row in rows:
        cells = row.split("\t")
        path_parts = cells[0].split("_")
        genes = [gene for gene in cells[2:] if gene != ""]
        for path_part in path_parts:
            for gene in genes:
                key = path_part + gene
                value = gene_in_path.get(key, 0)
                gene_in_path[key] = value + 1
    return gene_in_path


def count_paths_for_gene(gene_in_path: dict, gene: str, path_part: str) -> int:
    return gene_in_path.get(path_part + gene, 0)

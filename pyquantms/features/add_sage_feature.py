import click
import pyopenms as oms
import pandas as pd


@click.command("add_sage_feature")
@click.option("--idx_file", "-i", help="Input idXML file")
@click.option("--output_file", "-o", help="Output idXML file")
@click.option("--feat_file", "-f", help="Input feature table file")
def add_feature(idx_file: str, output_file: str, feat_file: str):
    """
    Add extra features in features idXML. Adding extra feature in Sage isn't known input for PSMFeatureExtractor

    :param idx_file: Original idXML file
    :param output_file: Outpuf file with the extra feature
    :param feat_file: Feature file from Sage
    :return: None
    """
    extra_feat = []
    feat = pd.read_csv(feat_file, sep='\t')
    for _, row in feat.iterrows():
        if row["feature_generator"] == 'psm_file':
            continue
        else:
            extra_feat.append(row["feature_name"])
    print("Adding extra feature: {}".format(extra_feat))
    protein_ids = []
    peptide_ids = []
    oms.IdXMLFile().load(idx_file, protein_ids, peptide_ids)
    SearchParameters = protein_ids[0].getSearchParameters()
    features = SearchParameters.getMetaValue("extra_features")
    extra_features = features + "," + ",".join(extra_feat)
    SearchParameters.setMetaValue("extra_features", extra_features)
    protein_ids[0].setSearchParameters(SearchParameters)
    oms.IdXMLFile().store(output_file, protein_ids, peptide_ids)
    print("Done")




import os
from utils import data_utils
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


def main():
    print("Debug Gaussian Mixture Model")
    # Input Data file paths
    nightlights_file = os.environ.get("DATA_PATH") + 'nightlights.csv'
    nightlights = pd.read_csv(nightlights_file)
    bin_labels = ['low', 'low medium', 'medium', 'high medium', 'high']
    nightlights = data_utils.gaussian_mixture_model(
        nightlights, n_components=5, bin_labels=bin_labels)
    for label in bin_labels:
        print(
            "Number of {} intensity pixels: {}".format(
                label, nightlights[nightlights['label']
                                   == label]['ntl2016'].count()
            )
        )


if __name__ == "__main__":
    main()

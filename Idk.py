import pandas as pd

final_df = pd.read_csv("/content/PRO-NASA-Exoplanet-Scraped-Data/final_scraped_data.csv")

archive_df = pd.read_csv("/content/PRO-NASA-Exoplanet-Scraped-Data/PSCompPars.csv")

#I know they are the wrong paths (not sure what to use)

final_df.head()

archive_df.head()

final_df.shape

archive_df.shape

archive_df["pl_name"] = archive_df["pl_name"].str.lower()
archive_df.head()

archive_df = archive_df.sort_values("pl_name")
archive_df.tail(10)

final_df.tail(10)

merged_df = pd.merge(final_df, archive_df, on="id")

merged_df.shape
merged_df.columns

merged_df.to_csv("merge_stars.csv")

from visual_studio import files
files.download("merge_stars.csv")
# Python Standard Libraries
from pathlib import Path
# External Libraries
import pandas as pd


def load_data_as_dataframe() -> list:
    """Loads data from Dataset as Dataframe

    Returns:
        list: List with 4 Dataframes (true, fake, true_meta, fake_meta)
    """    
    
    # Initialize Dataframes
    df_true = pd.DataFrame(columns=["Veracity", "News"])
    df_fake = pd.DataFrame(columns=["Veracity", "News"])
    df_true_meta = pd.DataFrame(columns=["Veracity", "Author", \
        "Link", "Category", "Date", "Tokens", "Words", "Types", \
        "Links Inside", "Words Uppercase", "Verbs", "Subjuntive\Imperative Verbs", \
        "Nouns", "Adjectives", "Adverbs", "Modal Verbs", "Singular\Second Personal Pronouns", \
        "Plural First Personal Pronouns", "Pronouns", "Pausality", "Characters", \
        "Average Sentence Length", "Average Word Length", "Percentage of Spelling Errors", \
        "Emotiveness", "Diversity"])
    df_fake_meta = pd.DataFrame(columns=["Veracity", "Author", \
        "Link", "Category", "Date", "Tokens", "Words", "Types", \
        "Links Inside", "Words Uppercase", "Verbs", "Subjuntive\Imperative Verbs", \
        "Nouns", "Adjectives", "Adverbs", "Modal Verbs", "Singular\Second Personal Pronouns", \
        "Plural First Personal Pronouns", "Pronouns", "Pausality", "Characters", \
        "Average Sentence Length", "Average Word Length", "Percentage of Spelling Errors", \
        "Emotiveness", "Diversity"])
    
    # Find Directories of Dataset
    dirs = Path("../data").glob("*/")
    for directory in dirs:
        # Veracity = True | False | True-meta | Fake-meta
        veracity = directory.stem
        # Get Files from Directories
        files = Path(directory).glob("*.txt")
        for file in files:
            data = file.read_text(encoding="utf-8")
            
            # Get index for Dataframe
            if "meta" in file.stem:
                id = int(file.stem.split("-")[0])
            else:
                id = int(file.stem)
                
            # Separate data for categories
            if veracity == "true":
                df_true.loc[id] = [veracity, data]
            elif veracity == "fake":
                df_fake.loc[id] = [veracity, data]
            else:
                data = data.split("\n")
                data.insert(0, veracity)
                if veracity == "true-meta-information":
                    df_true_meta.loc[id] = [*data]
                elif veracity == "fake-meta-information":
                    df_fake_meta.loc[id] = [*data]
    
    # Sort index for Dataframes
    df_true.sort_index()
    df_fake.sort_index()
    df_true_meta.sort_index()
    df_fake_meta.sort_index()        
            
    return [df_true, df_fake, df_true_meta, df_fake_meta]
    
import pandas as pd
from sklearn.model_selection import train_test_split

def partition_data(df, train_size=0.7, test_size=0.2, random_state=None):
    """
    Partitions the DataFrame into training, testing, and validation sets.

    Parameters:
    df (pd.DataFrame): The DataFrame to partition.
    train_size (float): The proportion of the dataset to include in the training set.
    test_size (float): The proportion of the dataset to include in the testing set.
    random_state (int, optional): Controls the shuffling applied to the data before applying the split.

    Returns:
    tuple: A tuple containing the training, testing, and validation DataFrames.
    """
    # First, split the data into training and temp (testing + validation)
    train_df, temp_df = train_test_split(df, train_size=train_size, random_state=random_state)

    # Calculate the proportion for validation set
    val_size = 1 - train_size - test_size

    # Now split the temp data into testing and validation sets
    test_df, val_df = train_test_split(temp_df, test_size=val_size/(val_size + test_size), random_state=random_state)

    return train_df, test_df, val_df
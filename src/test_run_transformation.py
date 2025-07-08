from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    transformer = DataTransformation()
    train_arr, test_arr, pkl_path = transformer.initiate_data_transformation(
        train_path="artifacts/train.csv",
        test_path="artifacts/test.csv"
    )

    print("✅ Transformation successful!")
    print("Train shape:", train_arr.shape)
    print("Test shape:", test_arr.shape)
    print("Preprocessor saved at:", pkl_path)

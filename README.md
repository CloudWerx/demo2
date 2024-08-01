## Red Dot Design Award Product Descriptions Preprocessing Script

This repository contains a Python script for preprocessing a dataset of Red Dot design award product descriptions. The script utilizes the Hugging Face Datasets library to load the data and prepares it for further analysis or storage in Google Cloud Storage (GCS).

### Functionality

The script performs the following tasks:

1. **Dataset Loading:** Loads the "red-dot-design-award-product-description" dataset from Hugging Face Datasets. This dataset is assumed to contain text descriptions of products along with additional information like product name and category.
2. **Text File Generation:** Extracts the text description for each product and creates a separate text file for each description.
3. **JSONL File Creation:** Creates a JSON Lines (JSONL) file containing a JSON object for each product. Each JSON object includes:
    * **Unique ID:** A unique identifier generated for each product description.
    * **Product Details:** Information like product name and category (extracted from the dataset).
    * **Description Reference:** Reference to the corresponding text file containing the full product description.
4. **GCS Upload (Optional):** Uploads both the JSONL file and the individual text files to a specified GCS bucket (requires configuring bucket name).
5. **Cleanup (Optional):** Deletes the local JSONL file and directory containing text files after successful upload (can be disabled).

### Usage

1. **Install Dependencies:**
    * Ensure you have Python and the required libraries installed (`pip install datasets google-cloud-storage`).
    * Configure your Google Cloud project and authentication for GCS upload (if applicable).

2. **Run the Script:**
    * Execute the script (`python preprocess_red_dot_data.py`).

**Note:** This script expects the dataset "red-dot-design-award-product-description" to be available on the Hugging Face Hub.

### Configuration (Optional)

* Modify the script (`preprocess_red_dot_data.py`) to configure the following:
    * `bucket_name`: Replace with your GCS bucket name for upload (leave empty to skip upload).
    * `clean_up`: Set to `False` to keep local files after upload.

### License

This script is provided under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use and modify it for your needs.

# Speaker-Profiling
This is a simple experiment to investigate if WavLM embeddings can be used to accurately classify Singaporean speakers by demographic attributes such as gender, age, ethnicity, and education level. 

## Repository Structure

### `preprocessing.py`
This script processes the raw audio recordings from the National Speech Corpus (NSC):
- Trims the first 5 minutes of each `.wav` file.
- Detects and merges non-silent segments.
- Splits merged audio into 20 clips of **10 seconds each** per speaker.
- Saves the clips into structured directories by speaker ID.

## `speaker_prediction.ipynb`
This  Jupyter Notebook performs the main analysis:
- Extracts 768-dim WavLM Base+ embeddings from each audio clip
- Visualises speaker distributions across demographic attributes
- Runs classification experiments:
    - Speaker-level stratification
    - Label encoding
    - Classifiers:
        - Logistic Regression
        - Random Forest
        - Naive Bayes
        - SVM
        - MLP
- Classification reports:
    - Gender
    - Age
    - Ethnicity
    - Education Level

## Results

### Clustering
![](https://github.com/daniel-023/Speaker-Profiling/blob/main/visualisations/ethnicity_plot.png)
![](https://github.com/daniel-023/Speaker-Profiling/blob/main/visualisations/gender_plot.png)

### Classification Accuracy (%)
|                     | Gender | Age    | Ethnicity | Education |
|---------------------|--------|--------|-----------|-----------|
| Logistic Regression | 96     | 55     | 71        | 40        |
| Random Forest       | 93     | 54     | 62        | **42**    |
| Naive Bayes         | 83     | 60     | 57        | 41        |
| SVM                 | 97     | **63** | **72**    | 41        |
| MLP                 | **99** | 60     | 64        | **42**    |
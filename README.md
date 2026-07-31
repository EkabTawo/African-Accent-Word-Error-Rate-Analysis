# African Accent Word Error Rate Analysis

## Overview
This undergraduate research project evaluates the performance of two commercial **Automatic Speech Recognition (ASR)** systems **Google Speech Recognition** and **IBM Watson Speech to Text**, on English accents from multiple African countries.
Using **Word Error Rate (WER)** as the primary evaluation metric, the study compares transcription accuracy across different African accents and analyses how factors such as **speech recognition engine**, **speaker gender**, and **accent variation** influence recognition performance.

---

## Objectives
  - Compare the transcription accuracy of Google Speech Recognition and IBM Watson Speech to Text.
  - Evaluate ASR performance across multiple African English accents.
  - Investigate the influence of speaker gender on speech recognition accuracy.
  - Measure transcription quality using Word Error Rate (WER).
  - Identify strengths and limitations of each ASR system when processing diverse African English accents.

---

## Technologies Used
  - Python
  - Google Speech Recognition API
  - IBM Watson Speech to Text
  - Natural Language Processing (NLP)
  - Word Error Rate (WER)
  - Speech Processing
  - Microsoft Excel

---

## Repository Structure
```text
African-Accent-Word-Error-Rate-Analysis/
│
├── src/
│   └── word_error_rate_analysis.py
│
├── data/
│
├── docs/
│   └── african_accent_word_error_rate_report.pdf
│
├── presentation/
│   └── african_accent_word_error_rate_presentation.pptx
│
└── README.md
```

---

## Methodology
  1. Collect speech recordings from speakers representing selected African countries.
  2. Categorise recordings by country and speaker gender.
  3. Process each recording using:
     - Google Speech Recognition
     - IBM Watson Speech to Text
  4. Generate automatic transcriptions from both ASR systems.
  5. Compare each generated transcript with manually verified reference transcriptions.
  6. Calculate Word Error Rate (WER) for every transcription.
  7. Compare the performance of both ASR systems across:
     - African countries
     - Speaker gender
     - Overall transcription accuracy
  8. Interpret the findings to identify patterns in ASR performance.

---

## Results
The study found noticeable differences in transcription accuracy between **Google Speech Recognition** and **IBM Watson Speech to Text**. Performance varied depending on the speech recognition engine, the speaker's gender, and the African English accent being analysed.

Word Error Rate (WER) provided a consistent basis for comparing both systems, revealing that recognition accuracy was not uniform across all countries or demographic groups. These findings highlight the importance of evaluating ASR systems on diverse speech datasets before deploying them in multilingual and multicultural environments.

---

## Key Contributions
  - Evaluated two commercial Automatic Speech Recognition systems.
  - Compared ASR performance across multiple African English accents.
  - Analysed the impact of speaker gender on transcription accuracy.
  - Applied Word Error Rate (WER) as a quantitative evaluation metric.
  - Identified performance variations across speech recognition engines and demographic groups.
  - Produced findings that contribute to understanding ASR performance in underrepresented linguistic communities.

---

## Academic Resources
  - **Research Report:** `docs/african_accent_word_error_rate_report.pdf`
  - **Presentation:** `presentation/african_accent_word_error_rate_presentation.pptx`

---

## Future Improvements
Potential extensions to this project include:
  - Evaluating additional speech recognition engines (e.g., OpenAI Whisper, Microsoft Azure Speech, Amazon Transcribe).
  - Expanding the dataset to include more African countries and regional dialects.
  - Increasing the number and diversity of speakers to improve statistical robustness.
  - Investigating the effect of background noise and recording quality on ASR performance.
  - Exploring modern deep learning approaches to improve speech recognition for African English accents.

---

## License
This project is licensed under the MIT License.

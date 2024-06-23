
# Portfolio of Kshitij Dhannoda

Welcome to my portfolio showcasing various projects I've worked on during my academic and professional journey.


#### How to Run

To run this Streamlit app locally:

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. Install Streamlit using pip:

   ```bash
   pip install streamlit
   ```

3. Clone this repository:

   ```bash
   git clone https://github.com/dkshitij29/stramlit_test.git
   cd stramlit_test
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

6. Once the app starts, open your web browser and go to `http://localhost:8501` to view the app.

#### Preparations

- Collected speech/acoustic signals.
- Transformed speech to text using the speech_to_text package version 6.6.2.
- Displayed the translated text on the Android device.

#### Output

- Added all necessary permissions in AndroidManifest.xml.
- Designed the UI of the app in the main activity XML.
- Edited MainActivity.java:
  - Initialized variables and functions such as TextViews, SpeechRecognizer object, MediaPlayer, and Recorder objects.
  - Implemented startRecording to begin voice recording and start the activity (request proper permissions first).
  - Implemented OnActivityResult to retrieve data and send transcribed results to TextView.
- Edited MediaPlayer object:
  - Created a new MediaPlayer object to playback audio, providing the file path of the audio recording.
  - Released the MediaPlayer object to pause playing.

#### Challenges

- Handling two mic inputs simultaneously.
- Transcribing directly from an audio file required format conversion and managing costs for Google Cloud API usage.

#### Tools and Technologies

Flutter, Dart, speech_to_text: ^6.6.2

#### Final Report

- **Presentation Deadline**: 4/15/2024. Show all the files, important classes, and functions.
- **Submission Deadline**: 4/19/2024. Include source code, slides, experimental results (audio and text files), and a recorded video (specific demos).
